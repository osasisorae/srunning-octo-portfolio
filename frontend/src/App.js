import './App.css';
import React, { Component } from 'react';
import axios from 'axios';


class App extends Component {

  state = {
    projects: []
  }

  componentDidMount() {
    this.getProjects();
  }

  getProjects() {
    axios
      .get('http://127.0.0.1:8000/api/v1/projects/')
      .then( res => {
        this.setState({ projects: res.data});
      })
      .catch( err => {
        console.log(err);
      });
  }

  render() {
    return (
      <div>
        {this.state.projects.map(item => (
          <div key={item.id}>
            <h1>{ item.title }</h1>
            <p>{ item.description }</p>
            <ul>
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
