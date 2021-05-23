import React, { useState, useEffect } from "react";
import "./Book.css";

function Book () {
    const [addressList, setAddressList] = useState([]);
    const [displayComponent, setDisplayComponent] = useState(null);
    const [sortedList, setSortedList] = useState([]);
    const [matchedList, setMatchingEntries] = useState([]);

    const getAddressList = () => {
        fetch('/getAddressList').then(response => response.json())
        .then(data => {
            setAddressList(data['Address list']);
            setDisplayComponent("addressList");
        })
    };

    const getSortedList = () => {
        fetch('/getSortedList').then(response => response.json())
        .then(list => {
            setSortedList(list['Sorted list']);
            setDisplayComponent("sortedList");
        })
    };

    const getMatchingEntries = () => {
        fetch("/getMatchedList").then(response => response.json())
        .then(list => {
            setMatchingEntries(list['Matched list']);
            setDisplayComponent("matchedList");
        })
    };

    useEffect(() => {
        fetch('/getAddressList').then(response => response.json())
        .then(data => {
            console.log(data);
            setAddressList(data['Address list']);
        })
    }, []);

    return (
        <div className="Book">
            <div className="header">
                <h1>{"Display of Address Book, Sorted List or List of Matches"}</h1>
            </div>
            <div className='buttons'>
            <div className="btn">
                <button onClick = {() => getAddressList()}>Display address book list</button>
            </div>

            <div className="btn">
                <button onClick = {() => getSortedList()}>Display sorted list</button>
            </div>

            <div className="btn">
                <button onClick = {() => getMatchingEntries()}>Display list of matches</button>
            </div>
            </div>
            
            {displayComponent === "addressList" && (
            <div className="Display">
                <h2 className="List-head"> Address list </h2>
                <div className="Display-content">
                    <ul>
                        {addressList.map((item) => (
                            <li>
                                First name: {item['First name']}, Last name: {item['Last name']}, Phone number: {item['Phone number']}
                            </li>
                        ))}
                    </ul>
                </div>    
            </div>
            )}

            {displayComponent === "sortedList" && (
            <div>
                <h2 className="List-head">Sorted list</h2>
                <div className="Display-content">
                    <ul>
                        {sortedList.map((item) => (
                            <li>
                                First name: {item['First name']}, Last name: {item['Last name']}, Phone number: {item['Phone number']}
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
            )}  

            {displayComponent === "matchedList" && (
            <div>
                <h2 className="List-head">Matched list</h2>
                <div className="Display-content">
                    <ul>
                        {matchedList.map((item) => (
                            <li>
                                First name: {item['First name']}, Last name: {item['Last name']}, Phone number: {item['Phone number']}
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
            )}
        </div>
    )
}

export default Book;