document.addEventListener('DOMContentLoaded', function() {
  var analyzeButton = document.getElementById('analyzeButton');
  var resultDiv = document.getElementById('result');

  analyzeButton.addEventListener('click', async function() {
    try {
      // Make a request to your local server (replace with your actual API endpoint)
      const response = await fetch('http://localhost:8052/');
      const data = await response.text(); // Assuming your server returns plain text

      // Display the result
      resultDiv.innerHTML = `<strong>Response from local server:</strong><br>${data}`;
    } catch (error) {
      resultDiv.innerHTML = `<strong>Error:</strong> ${error.message}`;
    }
  });
});
