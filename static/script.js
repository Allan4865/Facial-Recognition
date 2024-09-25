// Función para cargar el video en el elemento de imagen
function loadVideo() {
    fetch('/video_feed')
      .then(response => response.blob())
      .then(blob => {
        const objectURL = URL.createObjectURL(blob);
        const video = document.getElementById('video-stream');
        video.src = objectURL;
      })
      .catch(error => console.error('Error al cargar el video:', error));
  }
  
  // Cargar el video al cargar la página
  window.addEventListener('load', loadVideo);
  
  // Simulación de resultados
  const results = [
    { name: 'Persona 1', age: 25, gender: 'M' },
    { name: 'Persona 2', age: 32, gender: 'F' },
    { name: 'Persona 3', age: 19, gender: 'M' }
  ];
  
  // Función para generar los resultados HTML
  function generateResultsHTML() {
    const resultsContainer = document.getElementById('results-container');
    let resultsHTML = '';
  
    for (const result of results) {
      resultsHTML += `
        <div class="result-item">
          <p><strong>Nombre:</strong> ${result.name}</p>
          <p><strong>Edad:</strong> ${result.age}</p>
          <p><strong>Género:</strong> ${result.gender}</p>
        </div>
      `;
    }
  
    resultsContainer.innerHTML = resultsHTML;
  }
  
  // Generar los resultados al cargar la página
  window.addEventListener('load', generateResultsHTML);