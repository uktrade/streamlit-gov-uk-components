import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

class GovUkCheckbox extends StreamlitComponentBase {
  public render = (): ReactNode => {
    const label = this.props.args["label"]
    const id = this.props.args["id"]

    return (
      <div className="govuk-checkboxes" data-module="govuk-checkboxes">
        <div className="govuk-checkboxes__item">
          <input
            disabled={this.props.disabled}
            defaultChecked={this.props.args["default"]}
            onInput={this.onInput}
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

  private onInput = (event: React.ChangeEvent<HTMLInputElement>): void => {
    Streamlit.setComponentValue(event.target.checked)
  }
}

export default withStreamlitConnection(GovUkCheckbox)
