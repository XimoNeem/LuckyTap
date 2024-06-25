document.addEventListener('DOMContentLoaded', (event) => {
    const clickerButton = document.getElementById('clicker-button');
    const coinCountElement = document.querySelector('.coins .coin-count');
    
    async function getCoinCount() {
        const response = await fetch('/api/clicks');
        const data = await response.json();
        coinCountElement.textContent = "💰 " + data.count;
    }

    async function incrementCoinCount() {
        const response = await fetch('/api/clicks', { method: 'POST' });
        const data = await response.json();
        coinCountElement.textContent = "💰 " + data.count;
    }

    clickerButton.addEventListener('click', incrementCoinCount);

    getCoinCount();
});
