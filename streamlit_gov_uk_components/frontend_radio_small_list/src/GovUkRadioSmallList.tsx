import {
  ComponentProps,
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

interface State {
  selected: string | null
}

class GovUkRadioSmallList extends StreamlitComponentBase<State> {
  public constructor(props: ComponentProps) {
    super(props)

    const selected = this.props.args["default"]
    this.state = { selected }
  }

  public render = (): ReactNode => {
    return (
      <div className="govuk-radios govuk-radios--small" data-module="govuk-radios">
        {this.props.args["options"].map(([id, label]: [string, any]) =>
          <div className="govuk-radios__item" key={id}>
            <input
              disabled={this.props.disabled}
              checked={this.state.selected == id}
              onChange={(e) => this.onChange(id, e)}
              className="govuk-radios__input"
              id={this.props.args["id"] + '-' + id} name={id} value={id}
              type="radio"
            />
            <label className="govuk-label govuk-radios__label" htmlFor={this.props.args["id"] + '-' + id}>
              {label}
            </label>
          </div>
        )}
      </div>
    )
  }

  private onChange = (id: string, event: React.ChangeEvent<HTMLInputElement>): void => {
    const selected = event.target.value;
    this.setState(prevState => {
        return {selected: selected}
    }, () => {
      Streamlit.setComponentValue(this.state.selected)
    })
  }
}

export default withStreamlitConnection(GovUkRadioSmallList)
