import {
  ComponentProps,
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

interface State {
  selected: ReadonlySet<string>
}

class GovUkCheckboxSmallList extends StreamlitComponentBase<State> {
  public constructor(props: ComponentProps) {
    super(props)

    const selected = new Set<string>(this.props.args["default"])
    this.state = { selected }
  }

  public render = (): ReactNode => {
    return (
      <div className="govuk-checkboxes govuk-checkboxes--small" data-module="govuk-checkboxes">
        {this.props.args["options"].map(([id, label]: [string, any]) =>
          <div className="govuk-checkboxes__item" key={id}>
            <input
              disabled={this.props.disabled}
              checked={this.state.selected.has(id)}
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
        const newSet = new Set(prevState.selected)
        newSet[selected ? 'add' : 'delete'](id)
        return {selected: newSet}
    }, () => {
      // To be tidy, always return selected options in the order passed in options
      Streamlit.setComponentValue(this.props.args["options"].filter(([id, label]: [string, any]) =>
        this.state.selected.has(id)
      ).map(([id, label]: [string, any]) => id))
    })
  }
}

export default withStreamlitConnection(GovUkCheckboxSmallList)
