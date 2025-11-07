import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Plot from 'react-plotly.js'
import './App.css'

const API_BASE = 'http://localhost:5000/api'

interface SalaryData {
  Role_Name: string
  Country: string
  Team_Setup: string
  Salary_Min_USD: number
  Salary_Max_USD: number
  Salary_Avg_USD: number
  Skills?: string
  Experience_Level?: string
  Years_of_Experience?: number
}

interface Summary {
  total_records: number
  countries: string[]
  roles: string[]
  team_setups: string[]
  salary_stats: {
    min: number
    max: number
    avg: number
    median: number
    std: number
  }
}

interface CountryData {
  country: string
  avg_salary: number
  min_salary: number
  max_salary: number
  count: number
}

interface RoleData {
  role: string
  avg_salary: number
  min_salary: number
  max_salary: number
  count: number
}

interface ForecastData {
  year: string
  predicted_salary: number
  lower_bound: number
  upper_bound: number
}

interface EconomicData {
  country: string
  gdp_per_capita: number
  cost_of_living_index: number
  unemployment_rate: number
  inflation_rate: number
}

interface LegalData {
  country: string
  working_hours_per_week: number
  vacation_days: number
  minimum_wage: number
  tax_rate: number
  benefits: string[]
}

export default function App() {
  // Data state
  const [salaryData, setSalaryData] = useState<SalaryData[]>([])
  const [summary, setSummary] = useState<Summary | null>(null)
  const [countryData, setCountryData] = useState<CountryData[]>([])
  const [roleData, setRoleData] = useState<RoleData[]>([])
  const [forecastData, setForecastData] = useState<ForecastData[]>([])
  const [economicData, setEconomicData] = useState<EconomicData[]>([])
  const [legalData, setLegalData] = useState<LegalData[]>([])
  
  // Filter state (multiselect arrays - all selected by default)
  const [selectedCountries, setSelectedCountries] = useState<string[]>([])
  const [selectedRoles, setSelectedRoles] = useState<string[]>([])
  const [selectedTeamSetups, setSelectedTeamSetups] = useState<string[]>([])
  
  // UI state
  const [dataLoaded, setDataLoaded] = useState(false)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [activeTab, setActiveTab] = useState('overview')
  
  // Computed: Filtered data based on sidebar filters
  const filteredData = salaryData.filter(row => {
    const matchCountry = selectedCountries.length === 0 || selectedCountries.includes(row.Country)
    const matchRole = selectedRoles.length === 0 || selectedRoles.includes(row.Role_Name)
    const matchTeamSetup = selectedTeamSetups.length === 0 || selectedTeamSetups.includes(row.Team_Setup)
    return matchCountry && matchRole && matchTeamSetup
  })

  useEffect(() => {
    checkStatus()
  }, [])

  // Initialize filters when summary loads
  useEffect(() => {
    if (summary) {
      // Set all countries/roles/team_setups selected by default (like Streamlit)
      setSelectedCountries(summary.countries)
      setSelectedRoles(summary.roles)
      setSelectedTeamSetups(summary.team_setups)
    }
  }, [summary])

  const checkStatus = async () => {
    try {
      const response = await axios.get(`${API_BASE}/status`)
      if (response.data.data_loaded) {
        setDataLoaded(true)
        // Auto-load data if backend has data loaded
        await loadData()
      }
    } catch (err) {
      setError('Unable to connect to backend')
    }
  }

  const initializeDemoData = async () => {
    setLoading(true)
    setError(null)
    try {
      await axios.post(`${API_BASE}/init`)
      await loadData()
      setDataLoaded(true)
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to initialize data')
    } finally {
      setLoading(false)
    }
  }

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    setLoading(true)
    setError(null)
    const formData = new FormData()
    formData.append('file', file)

    try {
      await axios.post(`${API_BASE}/upload`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      await loadData()
      setDataLoaded(true)
      // Reset file input
      e.target.value = ''
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to upload file')
      // Reset file input on error too
      e.target.value = ''
    } finally {
      setLoading(false)
    }
  }

  const loadData = async () => {
    try {
      const [summaryRes, countryRes, roleRes, salaryRes, economicRes, legalRes] = await Promise.all([
        axios.get(`${API_BASE}/data/summary`),
        axios.get(`${API_BASE}/data/by-country`),
        axios.get(`${API_BASE}/data/by-role`),
        axios.get(`${API_BASE}/data/salaries`),
        axios.get(`${API_BASE}/economic`),
        axios.get(`${API_BASE}/legal`)
      ])

      setSummary(summaryRes.data)
      setCountryData(countryRes.data)
      setRoleData(roleRes.data)
      setSalaryData(salaryRes.data.data)
      
      // Handle backend response format {success: true, data: [...]}
      const economicDataArray = economicRes.data.data || economicRes.data
      const legalDataArray = legalRes.data.data || legalRes.data
      
      setEconomicData(Array.isArray(economicDataArray) ? economicDataArray : [])
      setLegalData(Array.isArray(legalDataArray) ? legalDataArray : [])
      
      console.log('✅ Data loaded successfully:', {
        summary: summaryRes.data.total_records,
        countries: countryRes.data.length,
        roles: roleRes.data.length,
        salaries: salaryRes.data.data.length,
        economic: economicDataArray.length,
        legal: legalDataArray.length
      })
    } catch (err: any) {
      console.error('❌ Failed to load data:', err)
      setError('Failed to load data: ' + (err.message || 'Unknown error'))
    }
  }

  const loadForecast = async () => {
    setLoading(true)
    try {
      const params = new URLSearchParams()
      // Use first selected country and role for forecast (or 'all' if none selected)
      if (selectedCountries.length > 0) params.append('country', selectedCountries[0])
      if (selectedRoles.length > 0) params.append('role', selectedRoles[0])
      
      const response = await axios.get(`${API_BASE}/forecast?${params}`)
      
      // Transform backend format to frontend format
      // Backend returns: {Country, Role_Name, Year_2025, Year_2026, ...}
      // Frontend needs: [{year, predicted_salary, lower_bound, upper_bound}, ...]
      
      const backendData = response.data.data || response.data
      if (backendData && backendData.length > 0) {
        // Take the first matching record or aggregate
        const record = backendData[0]
        const years = ['2025', '2026', '2027', '2028', '2029', '2030']
        
        const transformedData: ForecastData[] = years.map(year => {
          const predicted = record[`Year_${year}`] || 0
          return {
            year,
            predicted_salary: predicted,
            lower_bound: predicted * 0.9, // 10% confidence interval
            upper_bound: predicted * 1.1
          }
        })
        
        setForecastData(transformedData)
        console.log('✅ Forecast loaded:', transformedData.length, 'years')
      } else {
        setForecastData([])
        setError('No forecast data available for selected filters')
      }
    } catch (err: any) {
      console.error('❌ Failed to load forecast:', err)
      setError('Failed to load forecast: ' + (err.message || 'Unknown error'))
    } finally {
      setLoading(false)
    }
  }

  const formatCurrency = (value: number) => {
    const thousands = Math.round(value / 1000)
    return `€${thousands}K`
  }

  const renderOverview = () => {
    if (!summary) return null

    // Compute statistics from filtered data
    const filteredStats = {
      count: filteredData.length,
      avgSalary: filteredData.length > 0 
        ? filteredData.reduce((sum, d) => sum + d.Salary_Avg_USD, 0) / filteredData.length 
        : 0,
      minSalary: filteredData.length > 0 
        ? Math.min(...filteredData.map(d => d.Salary_Min_USD)) 
        : 0,
      maxSalary: filteredData.length > 0 
        ? Math.max(...filteredData.map(d => d.Salary_Max_USD)) 
        : 0
    }

    // Aggregate filtered data by country
    const countryAgg = filteredData.reduce((acc, row) => {
      if (!acc[row.Country]) {
        acc[row.Country] = { total: 0, count: 0 }
      }
      acc[row.Country].total += row.Salary_Avg_USD
      acc[row.Country].count += 1
      return acc
    }, {} as Record<string, { total: number, count: number }>)

    const filteredCountryData = Object.entries(countryAgg).map(([country, data]) => ({
      country,
      avg_salary: data.total / data.count
    })).sort((a, b) => b.avg_salary - a.avg_salary)

    // Aggregate filtered data by role
    const roleAgg = filteredData.reduce((acc, row) => {
      if (!acc[row.Role_Name]) {
        acc[row.Role_Name] = { total: 0, count: 0 }
      }
      acc[row.Role_Name].total += row.Salary_Avg_USD
      acc[row.Role_Name].count += 1
      return acc
    }, {} as Record<string, { total: number, count: number }>)

    const filteredRoleData = Object.entries(roleAgg).map(([role, data]) => ({
      role,
      avg_salary: data.total / data.count
    })).sort((a, b) => b.avg_salary - a.avg_salary).slice(0, 10) // Top 10 roles

    return (
      <div className="overview">
        <h2>Dashboard Overview</h2>
        <p className="info-text">Showing {filteredStats.count} records (filtered from {summary.total_records} total)</p>
        
        <div className="metrics-grid">
          <div className="metric-card">
            <h3>Filtered Records</h3>
            <p className="metric-value">{filteredStats.count.toLocaleString()}</p>
          </div>
          <div className="metric-card">
            <h3>Average Salary</h3>
            <p className="metric-value">{formatCurrency(filteredStats.avgSalary)}</p>
          </div>
          <div className="metric-card">
            <h3>Min Salary</h3>
            <p className="metric-value">{formatCurrency(filteredStats.minSalary)}</p>
          </div>
          <div className="metric-card">
            <h3>Max Salary</h3>
            <p className="metric-value">{formatCurrency(filteredStats.maxSalary)}</p>
          </div>
        </div>

        <div className="charts-grid">
          <div className="chart-container">
            <h3>Salary by Country (Filtered)</h3>
            <Plot
              data={[{
                x: filteredCountryData.map(d => d.country),
                y: filteredCountryData.map(d => d.avg_salary),
                type: 'bar',
                marker: { color: '#003087' }
              }]}
              layout={{
                title: '',
                xaxis: { title: 'Country' },
                yaxis: { title: 'Average Salary (USD)' },
                height: 400
              }}
              style={{ width: '100%' }}
              config={{ responsive: true }}
            />
          </div>

          <div className="chart-container">
            <h3>Top 10 Roles by Salary (Filtered)</h3>
            <Plot
              data={[{
                x: filteredRoleData.map(d => d.avg_salary),
                y: filteredRoleData.map(d => d.role),
                type: 'bar',
                orientation: 'h',
                marker: { color: '#0066cc' }
              }]}
              layout={{
                title: '',
                xaxis: { title: 'Average Salary (USD)' },
                yaxis: { title: 'Role' },
                height: 400
              }}
              style={{ width: '100%' }}
              config={{ responsive: true }}
            />
          </div>
        </div>
      </div>
    )
  }

  // Multiselect handlers
  const toggleCountrySelection = (country: string) => {
    setSelectedCountries(prev =>
      prev.includes(country) ? prev.filter(c => c !== country) : [...prev, country]
    )
  }

  const toggleRoleSelection = (role: string) => {
    setSelectedRoles(prev =>
      prev.includes(role) ? prev.filter(r => r !== role) : [...prev, role]
    )
  }

  const toggleTeamSetupSelection = (teamSetup: string) => {
    setSelectedTeamSetups(prev =>
      prev.includes(teamSetup) ? prev.filter(t => t !== teamSetup) : [...prev, teamSetup]
    )
  }

  const selectAllCountries = () => setSelectedCountries(summary?.countries || [])
  const clearAllCountries = () => setSelectedCountries([])
  const selectAllRoles = () => setSelectedRoles(summary?.roles || [])
  const clearAllRoles = () => setSelectedRoles([])
  const selectAllTeamSetups = () => setSelectedTeamSetups(summary?.team_setups || [])
  const clearAllTeamSetups = () => setSelectedTeamSetups([])

  const renderExplorer = () => {

    return (
      <div className="explorer">
        <h2>Salary Explorer</h2>
        <p className="info-text">Filtered by: {selectedCountries.length} countries, {selectedRoles.length} roles, {selectedTeamSetups.length} team setups ({filteredData.length} records)</p>

        <div className="table-container">
          <table className="data-table">
            <thead>
              <tr>
                <th>Role</th>
                <th>Country</th>
                <th>Team Setup</th>
                <th>Min Salary</th>
                <th>Avg Salary</th>
                <th>Max Salary</th>
              </tr>
            </thead>
            <tbody>
              {filteredData.map((row, idx) => (
                <tr key={idx}>
                  <td>{row.Role_Name}</td>
                  <td>{row.Country}</td>
                  <td>{row.Team_Setup}</td>
                  <td>{formatCurrency(row.Salary_Min_USD)}</td>
                  <td>{formatCurrency(row.Salary_Avg_USD)}</td>
                  <td>{formatCurrency(row.Salary_Max_USD)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    )
  }

  const renderForecast = () => {
    const forecastCountry = selectedCountries.length > 0 ? selectedCountries[0] : 'All Countries'
    const forecastRole = selectedRoles.length > 0 ? selectedRoles[0] : 'All Roles'
    
    return (
      <div className="forecast">
        <h2>5-Year Salary Forecast</h2>
        <p className="description">Machine learning predictions for salary trends based on historical data</p>
        <p className="info-text">Forecast for: {forecastCountry} - {forecastRole}</p>
        
        <div className="forecast-actions">
          <button onClick={loadForecast} className="btn btn-primary" disabled={loading}>
            {loading ? 'Generating...' : 'Generate Forecast'}
          </button>
        </div>

        {loading && <p className="loading">Loading forecast data...</p>}

        {!loading && forecastData.length > 0 && (
          <div className="chart-container">
            <h3>Salary Projection: {forecastCountry} - {forecastRole}</h3>
            <Plot
              data={[
                {
                  x: forecastData.map(d => d.year),
                  y: forecastData.map(d => d.predicted_salary),
                  type: 'scatter',
                  mode: 'lines+markers',
                  name: 'Predicted Salary',
                  line: { color: '#003087', width: 3 },
                  marker: { size: 8 }
                },
                {
                  x: forecastData.map(d => d.year),
                  y: forecastData.map(d => d.upper_bound),
                  type: 'scatter',
                  mode: 'lines',
                  name: 'Upper Bound',
                  line: { color: '#003087', width: 1, dash: 'dash' },
                  fill: 'tonexty',
                  fillcolor: 'rgba(0, 48, 135, 0.2)'
                },
                {
                  x: forecastData.map(d => d.year),
                  y: forecastData.map(d => d.lower_bound),
                  type: 'scatter',
                  mode: 'lines',
                  name: 'Lower Bound',
                  line: { color: '#003087', width: 1, dash: 'dash' }
                }
              ]}
              layout={{
                title: 'Salary Forecast (Next 5 Years)',
                xaxis: { title: 'Year' },
                yaxis: { title: 'Salary (USD)' },
                height: 500,
                showlegend: true
              }}
              style={{ width: '100%' }}
              config={{ responsive: true }}
            />
          </div>
        )}
      </div>
    )
  }

  const renderEconomic = () => {
    // Filter economic data based on selected countries
    const filteredEconomicData = economicData.filter(row => 
      selectedCountries.length === 0 || selectedCountries.includes(row.country)
    )

    return (
      <div className="economic">
        <h2>Economic Context</h2>
        <p className="description">Economic indicators for DevOps markets across countries</p>
        <p className="info-text">Showing {filteredEconomicData.length} countries (filtered by sidebar)</p>
        
        <div className="table-container">
          <table className="data-table">
            <thead>
              <tr>
                <th>Country</th>
                <th>GDP per Capita</th>
                <th>Cost of Living Index</th>
                <th>Unemployment Rate</th>
                <th>Inflation Rate</th>
              </tr>
            </thead>
            <tbody>
              {filteredEconomicData.map((row, idx) => (
                <tr key={idx}>
                  <td>{row.country}</td>
                  <td>${row.gdp_per_capita.toLocaleString()}</td>
                  <td>{row.cost_of_living_index}</td>
                  <td>{row.unemployment_rate}%</td>
                  <td>{row.inflation_rate}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="charts-grid">
          <div className="chart-container">
            <h3>GDP per Capita</h3>
            <Plot
              data={[{
                x: filteredEconomicData.map(d => d.country),
                y: filteredEconomicData.map(d => d.gdp_per_capita),
                type: 'bar',
                marker: { color: '#003087' }
              }]}
              layout={{
                xaxis: { title: 'Country' },
                yaxis: { title: 'GDP per Capita (USD)' },
                height: 400
              }}
              style={{ width: '100%' }}
              config={{ responsive: true }}
            />
          </div>

          <div className="chart-container">
            <h3>Cost of Living Index</h3>
            <Plot
              data={[{
                x: filteredEconomicData.map(d => d.country),
                y: filteredEconomicData.map(d => d.cost_of_living_index),
                type: 'bar',
                marker: { color: '#0066cc' }
              }]}
              layout={{
                xaxis: { title: 'Country' },
                yaxis: { title: 'Index' },
                height: 400
              }}
              style={{ width: '100%' }}
              config={{ responsive: true }}
            />
          </div>
        </div>
      </div>
    )
  }

  const renderLegal = () => {
    // Filter legal data based on selected countries
    const filteredLegalData = legalData.filter(row => 
      selectedCountries.length === 0 || selectedCountries.includes(row.country)
    )

    return (
      <div className="legal">
        <h2>Legal & Cultural Context</h2>
        <p className="description">Work regulations, benefits, and cultural factors across markets</p>
        <p className="info-text">Showing {filteredLegalData.length} countries (filtered by sidebar)</p>
        
        <div className="table-container">
          <table className="data-table">
            <thead>
              <tr>
                <th>Country</th>
                <th>Working Hours/Week</th>
                <th>Vacation Days</th>
                <th>Minimum Wage</th>
                <th>Tax Rate</th>
                <th>Benefits</th>
              </tr>
            </thead>
            <tbody>
              {filteredLegalData.map((row, idx) => (
                <tr key={idx}>
                  <td>{row.country}</td>
                  <td>{row.working_hours_per_week}</td>
                  <td>{row.vacation_days}</td>
                  <td>${row.minimum_wage.toLocaleString()}</td>
                  <td>{row.tax_rate}%</td>
                  <td>{row.benefits.join(', ')}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="charts-grid">
          <div className="chart-container">
            <h3>Vacation Days by Country</h3>
            <Plot
              data={[{
                x: filteredLegalData.map(d => d.country),
                y: filteredLegalData.map(d => d.vacation_days),
                type: 'bar',
                marker: { color: '#003087' }
              }]}
              layout={{
                xaxis: { title: 'Country' },
                yaxis: { title: 'Days per Year' },
                height: 400
              }}
              style={{ width: '100%' }}
              config={{ responsive: true }}
            />
          </div>

          <div className="chart-container">
            <h3>Tax Rates</h3>
            <Plot
              data={[{
                labels: filteredLegalData.map(d => d.country),
                values: filteredLegalData.map(d => d.tax_rate),
                type: 'pie',
                marker: {
                  colors: ['#003087', '#0066cc', '#0099ff', '#66ccff']
                }
              }]}
              layout={{
                height: 400
              }}
              style={{ width: '100%' }}
              config={{ responsive: true }}
            />
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="app-container">
      <header className="header">
        <h1>🚗 BMW DevOps Salary Dashboard</h1>
        <p className="subtitle">Euro Trends × ISM Field Project</p>
      </header>

      {error && <div className="error-banner">{error}</div>}

      {!dataLoaded ? (
        <div className="upload-section">
          <div className="upload-card">
            <h2>Get Started</h2>
            <p>Upload a dataset or initialize with demo data to view the dashboard.</p>
            
            <button onClick={initializeDemoData} disabled={loading} className="btn btn-primary">
              {loading ? 'Loading...' : 'Load Demo Data'}
            </button>

            <div className="divider">OR</div>

            <label className="file-upload">
              <input 
                type="file" 
                accept=".csv,.xlsx" 
                onChange={handleFileUpload}
                disabled={loading}
              />
              <span className="btn btn-secondary">Upload CSV/Excel File</span>
            </label>
          </div>
        </div>
      ) : (
        <div className="app-layout">
          {/* Sidebar - like Streamlit */}
          <aside className="sidebar">
            <div className="sidebar-section">
              <h3>Data Upload</h3>
              <div className="info-banner">
                ℹ️ Using demo data ({salaryData.length} records). Upload a file to replace.
              </div>
              <label className="file-upload-sidebar">
                <input 
                  type="file" 
                  accept=".csv,.xlsx" 
                  onChange={handleFileUpload}
                  disabled={loading}
                />
                <span className="btn btn-secondary btn-block">Choose File</span>
              </label>
            </div>

            <div className="sidebar-section">
              <h3>Filters</h3>
              
              {/* Countries Multiselect */}
              <div className="filter-group">
                <label className="filter-label">Select Countries</label>
                <div className="multiselect-actions">
                  <button className="link-button" onClick={selectAllCountries}>Select All</button>
                  <span className="action-divider">|</span>
                  <button className="link-button" onClick={clearAllCountries}>Clear</button>
                </div>
                <div className="multiselect-box">
                  {summary?.countries.map(country => (
                    <label key={country} className="checkbox-label">
                      <input
                        type="checkbox"
                        checked={selectedCountries.includes(country)}
                        onChange={() => toggleCountrySelection(country)}
                      />
                      <span>{country}</span>
                    </label>
                  ))}
                </div>
                <div className="filter-count">{selectedCountries.length} selected</div>
              </div>

              {/* Roles Multiselect */}
              <div className="filter-group">
                <label className="filter-label">Select Roles</label>
                <div className="multiselect-actions">
                  <button className="link-button" onClick={selectAllRoles}>Select All</button>
                  <span className="action-divider">|</span>
                  <button className="link-button" onClick={clearAllRoles}>Clear</button>
                </div>
                <div className="multiselect-box">
                  {summary?.roles.map(role => (
                    <label key={role} className="checkbox-label">
                      <input
                        type="checkbox"
                        checked={selectedRoles.includes(role)}
                        onChange={() => toggleRoleSelection(role)}
                      />
                      <span>{role}</span>
                    </label>
                  ))}
                </div>
                <div className="filter-count">{selectedRoles.length} selected</div>
              </div>

              {/* Team Setup Multiselect */}
              <div className="filter-group">
                <label className="filter-label">Select Team Setup</label>
                <div className="multiselect-actions">
                  <button className="link-button" onClick={selectAllTeamSetups}>Select All</button>
                  <span className="action-divider">|</span>
                  <button className="link-button" onClick={clearAllTeamSetups}>Clear</button>
                </div>
                <div className="multiselect-box">
                  {summary?.team_setups.map(setup => (
                    <label key={setup} className="checkbox-label">
                      <input
                        type="checkbox"
                        checked={selectedTeamSetups.includes(setup)}
                        onChange={() => toggleTeamSetupSelection(setup)}
                      />
                      <span>{setup}</span>
                    </label>
                  ))}
                </div>
                <div className="filter-count">{selectedTeamSetups.length} selected</div>
              </div>
            </div>
          </aside>

          {/* Main Content - like Streamlit's main area */}
          <main className="main-content">
            <nav className="tabs">
              <button 
                className={activeTab === 'overview' ? 'tab active' : 'tab'}
                onClick={() => setActiveTab('overview')}
              >
                Overview
              </button>
              <button 
                className={activeTab === 'explorer' ? 'tab active' : 'tab'}
                onClick={() => setActiveTab('explorer')}
              >
                Salary Explorer
              </button>
              <button 
                className={activeTab === 'forecast' ? 'tab active' : 'tab'}
                onClick={() => setActiveTab('forecast')}
              >
                5-Year Forecast
              </button>
              <button 
                className={activeTab === 'economic' ? 'tab active' : 'tab'}
                onClick={() => setActiveTab('economic')}
              >
                Economic Context
              </button>
              <button 
                className={activeTab === 'legal' ? 'tab active' : 'tab'}
                onClick={() => setActiveTab('legal')}
              >
                Legal & Cultural
              </button>
            </nav>

            <div className="tab-content">
              {activeTab === 'overview' && renderOverview()}
              {activeTab === 'explorer' && renderExplorer()}
              {activeTab === 'forecast' && renderForecast()}
              {activeTab === 'economic' && renderEconomic()}
              {activeTab === 'legal' && renderLegal()}
            </div>
          </main>
        </div>
      )}

      <footer className="footer">
        <p>© 2025 BMW × ISM | DevOps Salary Mapping Project</p>
      </footer>
    </div>
  )
}
