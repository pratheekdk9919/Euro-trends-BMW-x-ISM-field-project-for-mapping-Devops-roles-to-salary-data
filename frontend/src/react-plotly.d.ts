declare module 'react-plotly.js' {
  import { Component } from 'react';
  import { PlotParams } from 'plotly.js';

  interface PlotProps extends Partial<PlotParams> {
    data: Partial<PlotParams['data']>;
    layout?: Partial<PlotParams['layout']>;
    config?: Partial<PlotParams['config']>;
    frames?: Partial<PlotParams['frames']>;
    style?: React.CSSProperties;
    className?: string;
    divId?: string;
    onInitialized?: (figure: Readonly<PlotParams>, graphDiv: HTMLElement) => void;
    onUpdate?: (figure: Readonly<PlotParams>, graphDiv: HTMLElement) => void;
    onPurge?: (figure: Readonly<PlotParams>, graphDiv: HTMLElement) => void;
    onError?: (err: Error) => void;
    useResizeHandler?: boolean;
    debug?: boolean;
    onClickAnnotation?: (event: any) => void;
    onLegendClick?: (event: any) => boolean;
    onLegendDoubleClick?: (event: any) => boolean;
  }

  export default class Plot extends Component<PlotProps> {}
}
