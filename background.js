// Your background script logic goes here
console.log('Background script loaded.');

async function fetchDataFromLocalServer() {
  const apiUrl = 'http://localhost:8502/'; // Replace with your local server URL

  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.text(); // Assuming your server returns plain text
    return data;
  } catch (error) {
    console.error('Error:', error);
    return 'Error fetching data from local server';
  }
}

document.addEventListener('DOMContentLoaded', async function() {
  var analyzeButton = document.getElementById('analyzeButton');
  var resultDiv = document.getElementById('result');

  analyzeButton.addEventListener('click', async function() {
    const response = await fetchDataFromLocalServer();
    resultDiv.innerHTML = `<strong>Response from local server:</strong><br>${response}`;
  });
});
