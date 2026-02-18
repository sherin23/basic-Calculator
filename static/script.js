let currentInput = '';
const display = document.getElementById('display');

function appendToDisplay(value) {
    if (value === 'AC') {
        clearDisplay();
    } else if (value === 'DEL') {
        deleteLast();
    } else {
        currentInput += value;
        display.value = currentInput;
    }
}

function clearDisplay() {
    currentInput = '';
    display.value = '';
}

function deleteLast() {
    currentInput = currentInput.slice(0, -1);
    display.value = currentInput;
}

async function calculate() {
    if (!currentInput) return;

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: currentInput }),
        });

        const data = await response.json();
        
        if (response.ok) {
            display.value = data.result;
            currentInput = data.result; // Allow chaining calculations
        } else {
            display.value = 'Error';
            currentInput = '';
        }
    } catch (error) {
        console.error('Error:', error);
        display.value = 'Error';
        currentInput = '';
    }
}
