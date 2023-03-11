import logo from './logo.svg';
import './App.css';

const projects = [
  {"id":1,"title":"Test One","description":"Description One","start_date":"2022-10-01","end_date":"null","is_ongoing":true,"created_at":"2023-03-07T14:23:38.508537Z"},
  {"id":2,"title":"Test Two","description":"Project Test Two","start_date":"2020-10-01","end_date":"2022-06-01","is_ongoing":false,"created_at":"2023-03-07T14:24:19.138213Z"}
]

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
