import React from "react";
import Chart from "./Chart";
import { Selection } from "./Selection";
import { getData } from "./utils";
import Chip from "@material-ui/core/Chip";

export class HomePage extends React.Component {
  componentDidMount() {
    getData().then((data) => {
      this.setState({ data });
    });
  }

  render() {
    if (this.state == null) {
      return <div>Loading...</div>;
    }
    return (
      <div>
        <div style={{ display: "flex", alignItems: "center" }}>
          <Selection class="selection" />
          {["VIC"].map((item) => (
            <Chip style={{ marginLeft: 10 }} label={item} onDelete={() => {}} />
          ))}
        </div>
        <div class="chart">
          <Chart data={this.state.data} />
          {/* <Chart data={this.state.data} /> */}
        </div>
      </div>
    );
  }
}
