import {
  ComponentProps,
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

interface State {
  selected: boolean
}

class GovUkCheckbox extends StreamlitComponentBase<State> {
  public constructor(props: ComponentProps) {
    super(props)

    const selected = this.props.args["default"] as boolean
    this.state = { selected }
  }

  public render = (): ReactNode => {
    const label = this.props.args["label"]
    const id = this.props.args["id"]

    return (
      <div className="govuk-checkboxes" data-module="govuk-checkboxes">
        <div className="govuk-checkboxes__item">
          <input
            disabled={this.props.disabled}
            checked={this.state.selected}
            onChange={this.onChange}
            className="govuk-checkboxes__input"
            id={id} name={id}
            type="checkbox"
          />
          <label className="govuk-label govuk-checkboxes__label" htmlFor={id}>
            {label}
          </label>
        </div>
      </div>
    )
  }

  private onChange = (event: React.ChangeEvent<HTMLInputElement>): void => {
    const selected = event.target.checked;
    this.setState({ selected }, () => {
      Streamlit.setComponentValue(selected)
    })
  }
}

export default withStreamlitConnection(GovUkCheckbox)
