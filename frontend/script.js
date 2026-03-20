let searchType = 'tops'; // default

document.getElementById('topsBtn').addEventListener('click', () => {
    searchType = 'tops';
    document.getElementById('topsBtn').classList.add('active');
    document.getElementById('bottomsBtn').classList.remove('active');
    document.querySelector('.top-measurements').style.display = 'block';
    document.querySelector('.bottom-measurements').style.display = 'none';
});

document.getElementById('bottomsBtn').addEventListener('click', () => {
    searchType = 'bottoms';
    document.getElementById('bottomsBtn').classList.add('active');
    document.getElementById('topsBtn').classList.remove('active');
    document.querySelector('.top-measurements').style.display = 'none';
    document.querySelector('.bottom-measurements').style.display = 'block';
});

document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const dimensions = {
        size: document.getElementById('size').value,
        chest: document.getElementById('chest').value,
        waist: document.getElementById('waist').value,
        neck: document.getElementById('neck').value,
        sleeve: document.getElementById('sleeve').value,
        inseam: document.getElementById('inseam').value
    };

    const description = document.getElementById('description').value;

    if (!description || !dimensions.size) {
        alert('Please select a size and enter a description');
        return;
    }

    try {
        const response = await fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ dimensions, description, type: searchType })
        });

        const data = await response.json();

        if (response.ok) {
            displayResults(data);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to search');
    }
});

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    
    if (data.results.length === 0) {
        resultsDiv.innerHTML = '<p>No results found</p>';
        return;
    }

    let html = `<h2>Results (${data.total} found)</h2>`;
    html += `<p>Search: ${data.query} | Size: ${data.dimensions.size} | Type: ${data.type}</p>`;
    html += '<div class="results-grid">';

    data.results.forEach(item => {
        html += `
            <div class="result-card">
                <h3>${item.brand}</h3>
                <p><strong>Size:</strong> ${item.size}</p>
                <p><strong>Chest:</strong> ${item.measurements.chest ? item.measurements.chest[0] + '-' + item.measurements.chest[1] : 'N/A'}"</p>
                <p><strong>Waist:</strong> ${item.measurements.waist ? item.measurements.waist[0] + '-' + item.measurements.waist[1] : 'N/A'}"</p>
                <p><strong>Neck:</strong> ${item.measurements.neck ? item.measurements.neck[0] + '-' + item.measurements.neck[1] : 'N/A'}"</p>
                <p><strong>Sleeve:</strong> ${item.measurements.sleeve ? item.measurements.sleeve[0] + '-' + item.measurements.sleeve[1] : 'N/A'}"</p>
                <p><strong>Inseam:</strong> ${item.measurements.inseam ? item.measurements.inseam[0] + '-' + item.measurements.inseam[1] : 'N/A'}"</p>
                <p><strong>Type:</strong> ${item.type.join(', ')}</p>
            </div>
        `;
    });

    html += '</div>';
    resultsDiv.innerHTML = html;
}