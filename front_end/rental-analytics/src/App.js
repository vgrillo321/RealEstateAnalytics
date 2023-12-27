// import Component from the react module
import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from 'axios'; 
import logo from './logo.svg';
import './App.css';
import Select from 'react-select';

const unitedStatesList = [
  { name: 'ALABAMA', abbreviation: 'AL'},
  { name: 'ALASKA', abbreviation: 'AK'},
  { name: 'AMERICAN SAMOA', abbreviation: 'AS'},
  { name: 'ARIZONA', abbreviation: 'AZ'},
  { name: 'ARKANSAS', abbreviation: 'AR'},
  { name: 'CALIFORNIA', abbreviation: 'CA'},
  { name: 'COLORADO', abbreviation: 'CO'},
  { name: 'CONNECTICUT', abbreviation: 'CT'},
  { name: 'DELAWARE', abbreviation: 'DE'},
  { name: 'DISTRICT OF COLUMBIA', abbreviation: 'DC'},
  { name: 'FEDERATED STATES OF MICRONESIA', abbreviation: 'FM'},
  { name: 'FLORIDA', abbreviation: 'FL'},
  { name: 'GEORGIA', abbreviation: 'GA'},
  { name: 'GUAM', abbreviation: 'GU'},
  { name: 'HAWAII', abbreviation: 'HI'},
  { name: 'IDAHO', abbreviation: 'ID'},
  { name: 'ILLINOIS', abbreviation: 'IL'},
  { name: 'INDIANA', abbreviation: 'IN'},
  { name: 'IOWA', abbreviation: 'IA'},
  { name: 'KANSAS', abbreviation: 'KS'},
  { name: 'KENTUCKY', abbreviation: 'KY'},
  { name: 'LOUISIANA', abbreviation: 'LA'},
  { name: 'MAINE', abbreviation: 'ME'},
  { name: 'MARSHALL ISLANDS', abbreviation: 'MH'},
  { name: 'MARYLAND', abbreviation: 'MD'},
  { name: 'MASSACHUSETTS', abbreviation: 'MA'},
  { name: 'MICHIGAN', abbreviation: 'MI'},
  { name: 'MINNESOTA', abbreviation: 'MN'},
  { name: 'MISSISSIPPI', abbreviation: 'MS'},
  { name: 'MISSOURI', abbreviation: 'MO'},
  { name: 'MONTANA', abbreviation: 'MT'},
  { name: 'NEBRASKA', abbreviation: 'NE'},
  { name: 'NEVADA', abbreviation: 'NV'},
  { name: 'NEW HAMPSHIRE', abbreviation: 'NH'},
  { name: 'NEW JERSEY', abbreviation: 'NJ'},
  { name: 'NEW MEXICO', abbreviation: 'NM'},
  { name: 'NEW YORK', abbreviation: 'NY'},
  { name: 'NORTH CAROLINA', abbreviation: 'NC'},
  { name: 'NORTH DAKOTA', abbreviation: 'ND'},
  { name: 'NORTHERN MARIANA ISLANDS', abbreviation: 'MP'},
  { name: 'OHIO', abbreviation: 'OH'},
  { name: 'OKLAHOMA', abbreviation: 'OK'},
  { name: 'OREGON', abbreviation: 'OR'},
  { name: 'PALAU', abbreviation: 'PW'},
  { name: 'PENNSYLVANIA', abbreviation: 'PA'},
  { name: 'PUERTO RICO', abbreviation: 'PR'},
  { name: 'RHODE ISLAND', abbreviation: 'RI'},
  { name: 'SOUTH CAROLINA', abbreviation: 'SC'},
  { name: 'SOUTH DAKOTA', abbreviation: 'SD'},
  { name: 'TENNESSEE', abbreviation: 'TN'},
  { name: 'TEXAS', abbreviation: 'TX'},
  { name: 'UTAH', abbreviation: 'UT'},
  { name: 'VERMONT', abbreviation: 'VT'},
  { name: 'VIRGIN ISLANDS', abbreviation: 'VI'},
  { name: 'VIRGINIA', abbreviation: 'VA'},
  { name: 'WASHINGTON', abbreviation: 'WA'},
  { name: 'WEST VIRGINIA', abbreviation: 'WV'},
  { name: 'WISCONSIN', abbreviation: 'WI'},
  { name: 'WYOMING', abbreviation: 'WY' }
];


class App extends Component {
 
  // add a constructor to take props
  constructor(props) {
    super(props);
     
    // add the props here
    this.state = {
     
      // the viewCompleted prop represents the status
      // of the task. Set it to false by default
      viewCompleted: false,
      activeItem: {
        address: "",
        price: "",
        size: "",
        pricePerSqft: "",
      },
      
      function addCityState() {
        var city = document.getElementById('city').value;
        var state = document.getElementById('state').value;

        document.getElementById('city').value = '';
        document.getElementById('state').value = '';

        // Send data to the backend (replace the URL with your actual backend endpoint)
        fetch('/your-backend-endpoint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ city, state }),
        })
        .then(response => response.json())
        .then(data => {
            // Update the table with the new data
            updateTable(data);
        })
        .catch(error => console.error('Error:', error));
    }

    function updateTable(data) {
        var tableBody = document.getElementById('tableBody');
        // Clear existing rows
        tableBody.innerHTML = '';

        // Add new rows based on the received data
        data.forEach(entry => {
            var newRow = tableBody.insertRow(tableBody.rows.length);
            var cell1 = newRow.insertCell(0);
            var cell2 = newRow.insertCell(1);
            cell1.innerHTML = entry.city;
            cell2.innerHTML = entry.state;
        });
    }

    // Fetch initial data from the backend when the page loads
    fetch('/initial-backend-data')
        .then(response => response.json())
        .then(data => {
            // Update the table with the initial data
            updateTable(data);
        })
        .catch(error => console.error('Error:', error));
      // this list stores all the completed tasks
      propertyList: []
    };
  }

  // Add componentDidMount()
  componentDidMount() {
    this.refreshList();
  }
   
    
  refreshList = () => {
    axios   //Axios to send and receive HTTP requests
      .get("http://localhost:8000/api/property/")
      .then(res => this.setState({ propertyList: res.data }))
      .catch(err => console.log(err));
  };

// this arrow function takes status as a parameter
// and changes the status of viewCompleted to true
// if the status is true, else changes it to false

  // displayCompleted = status => {
  //   if (status) {
  //     return this.setState({ viewCompleted: true });
  //   }
  //   return this.setState({ viewCompleted: false });
  // };

    // this array function renders two spans that help control
  // the set of items to be displayed(ie, completed or incomplete)
  // renderTabList = () => {
  //   return (
  //     <div className="my-5 tab-list">
  //       <span
  //         onClick={() => this.displayCompleted(true)}
  //         className={this.state.viewCompleted ? "active" : ""}
  //       >
  //         completed
  //           </span>
  //       <span
  //         onClick={() => this.displayCompleted(false)}
  //         className={this.state.viewCompleted ? "" : "active"}
  //       >
  //         Incompleted
  //           </span>
  //     </div>
  //   );
  // };

  // Main variable to render items on the screen
  // TODO: Change this to render items in the list from script
  renderItems = () => {
    // const { viewCompleted } = this.state;
    const newItems = this.state.taskList.filter(
      (item) => item.completed === viewCompleted
    );
    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.description}
        >
          {item.title}
        </span>
        <span>
          <button
            onClick={() => this.editItem(item)}
            className="btn btn-secondary mr-2"
          >
            Edit
          </button>
          <button
            onClick={() => this.handleDelete(item)}
            className="btn btn-danger"
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to the rental analytics platform
        </p>
      </header>
      <div className="App-body">
        {/*TODO: Adding form to get city and state from user to pass to backend script */}
        <form action="">
            {/* City name as text input */}
          <div className='App-form'>
              <label for="fcity">City: </label>
              <input type="text" id="fcity" name="fcity"></input>
            </div>
            {/* TODO: States on list item, pass abbreviation to script */}
            <div className='App-form'>
              <label for="fstate">State: </label>
              <Select options={unitedStatesList}
                      getOptionLabel={(options) => options['name']} 
                      onChange={opt => console.log(opt.name, opt.abbreviation)} /> 
            </div>
          </form> 
        <div className="App-table">
          <table>
            <tr>
                <th>Address</th>
                <th>Price</th>
                <th>Size</th>
                <th>Price per Sqft</th>
            </tr>
            {testingData.map((val, key) => {
                return (
                    <tr key={key}>
                        <td>{val.address}</td>
                        <td>${val.price}</td>
                        <td>{val.size}sqft</td>
                        <td>${val.pricePerSqft}</td>
                    </tr>
                )
            })}
        </table>
        </div>
        <p>The average price per sqft in the area is {averagePricePerSqft}</p>
      </div>
    </div>
  );
}

export default App;
