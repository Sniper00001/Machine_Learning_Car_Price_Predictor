async function predictPrice(carName, company, year, fuel_type) {
    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                carName: carName,
                company: company,
                year: year,
                fuel_type: fuel_type
            })
        })

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        return result.predictions; 

    } catch (error) {
        console.error('Error:', error); 
        return ['Error occurred'];
    }
}
