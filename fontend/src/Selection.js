import React, { Component } from "react";

import AsyncSelect from "react-select/async";

const colourOptions = [
  { label: "fasdf" },
  { label: "cccccccccccccc" },
  { label: "eeeeeeeee" },
  { label: "fasdggggggggf" },
];

const customStyles = {
  container: () => ({
    width: 450,
    marginLeft: 70,
    zIndex: 1,
  }),
  menu: () => ({
    width: 450,
    position: "absolute",
    backgroundColor: "#FFF",
    zIndex: 9999,
  }),
};

export class Selection extends Component {
  state = { inputValue: "", listSelected: [] };

  handleInputChange = (newValue) => {
    const inputValue = newValue.replace(/\W/g, "");
    this.setState({ inputValue });
  };

  filterColors = (inputValue) => {
    console.log(inputValue);
    return colourOptions.filter((i) =>
      i.label.toLowerCase().includes(inputValue.toLowerCase())
    );
  };

  loadOptions = (inputValue, callback) => {
    console.log(inputValue);
    setTimeout(() => {
      callback(this.filterColors(inputValue));
    }, 1000);
  };

  handleChange = (selectedOption) => {
    const listSelected = [...this.state.listSelected, selectedOption];
    this.setState({ listSelected, inputValue: "" });
    console.log(`Option selected:`, listSelected);
  };

  render() {
    return (
      <div>
        <AsyncSelect
          styles={customStyles}
          loadOptions={this.loadOptions}
          onInputChange={this.handleInputChange}
          onChange={this.handleChange}
          value={this.state.inputValue}
          placeholder="Search company..."
        />
      </div>
    );
  }
}
