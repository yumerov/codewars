pragma solidity ^0.4.13;

contract HelloWorld {
  // State Variables
  string greeting = "Hello World!"; // Change this

  function setGreeting(string _greeting) {
      greeting = _greeting;
  }

  function greet() constant returns (string){
    return greeting;
  }
}