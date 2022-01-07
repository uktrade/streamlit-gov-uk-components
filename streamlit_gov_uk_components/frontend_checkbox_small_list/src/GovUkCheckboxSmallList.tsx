import {
  ComponentProps,
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

interface State {
  selected: { [key: string]: boolean }
}

class GovUkCheckboxSmallList extends StreamlitComponentBase<State> {
  public constructor(props: ComponentProps) {
    super(props)

    const selected = this.props.args["default"] as { [key: string]: boolean }
    this.state = { selected }
  }

  public render = (): ReactNode => {
    return (
      <div className="govuk-checkboxes govuk-checkboxes--small" data-module="govuk-checkboxes">
        {Object.entries(this.props.args["options"]).map(([id, label]: [string, any], index) =>
          <div className="govuk-checkboxes__item" key={id}>
            <input
              disabled={this.props.disabled}
              checked={this.state.selected[id]}
              onChange={(e) => this.onChange(id, e)}
              className="govuk-checkboxes__input"
              id={id} name={id}
              type="checkbox"
            />
            <label className="govuk-label govuk-checkboxes__label" htmlFor={id}>
              {label}
            </label>
          </div>
        )}
      </div>
    )
  }

  private onChange = (id: string, event: React.ChangeEvent<HTMLInputElement>): void => {
    const selected = event.target.checked;
    this.setState(prevState => {
      selected: Object.assign(prevState.selected, {[id]: selected})      
    }, () => {
      Streamlit.setComponentValue(this.state.selected)
    })
  }
}

export default withStreamlitConnection(GovUkCheckboxSmallList)
