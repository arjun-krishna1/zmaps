import './App.css';

const TableHeader = () => {
  return (
    <thead>
      <tr>
        <th>Location</th>
        <th>Type of Landmark</th>
      </tr>
    </thead>
  )
}
const TableBody = props => {
  const rows = props.data.locations_of_interest.map((row, index) => {
    return (
      <tr key={index}>
        <td>{row.location}</td>
        <td>{row.type_of_landmark}</td>
      </tr>
    )
  })
  return rows;

}
function App() {
  const temp = {
    "locations_of_interest":
    [
      {
        "uid":"cc76468d-42ea-4c05-bd7a-ebefb1058eb5",
        "location":"Simcoe",
        "type_of_landmark":"zombie horde",
        "location_info":
          {
            "uid":"02791652-c82f-4f7a-a956-891a9fcf1bd6",
            "number_of_zombies":39,
            "average_stage_of_decomposition":3
          }
        }
      ]
    }
  return (
    <div className="App">
      <header className="App-header">
        <div class="navbar">
          zmaps | World Anti-Zombie Federation
        </div>
        <body>
          <table>
            <TableHeader />
            <TableBody data={temp} />

          </table>
        </body>
      </header>
    </div>
  );
}

export default App;
