import './App.css';
import React, { Component } from 'react';

const projects = [
  {"id":1,"title":"Test One","description":"Description One","start_date":"2022-10-01","end_date":"null","is_ongoing":true,"created_at":"2023-03-07T14:23:38.508537Z"},
  {"id":2,"title":"Test Two","description":"Project Test Two","start_date":"2020-10-01","end_date":"2022-06-01","is_ongoing":false,"created_at":"2023-03-07T14:24:19.138213Z"}
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { projects };
  }

  render() {
    return (
      <div>
        {this.state.projects.map(item => (
          <div key={item.id}>
            <h1>{ item.title }</h1>
            <p>{ item.description }</p>
            <ul>
              <li>{ item.is_ongoing }</li>
              <li>{ item.start_date }</li>
              <li>{ item.end_date }</li>
            </ul>
          </div>
        ))}
      </div>
    )
  }
}

export default App;
