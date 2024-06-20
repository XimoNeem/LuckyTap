document.addEventListener('DOMContentLoaded', (event) => {
    let count = 0;
    const clickCountElement = document.getElementById('click-count');
    const clickerButton = document.getElementById('clicker-button');

    clickerButton.addEventListener('click', () => {
        count++;
        clickCountElement.textContent = count;
    });
});