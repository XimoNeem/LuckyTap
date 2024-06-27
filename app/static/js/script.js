document.addEventListener('DOMContentLoaded', (event) => {
    const clickerButton = document.getElementById('clicker-button');
    const walletButton = document.getElementById('wallet-button');
    const coinCountElement = document.querySelector('.coins .coin-count');
    
    async function getCoinCount() {
        const response = await fetch('/api/clicks');
        const data = await response.json();
        coinCountElement.textContent = data.count;
    }

    async function incrementCoinCount() {
        const response = await fetch('/api/clicks', { method: 'POST' });
        const data = await response.json();
        coinCountElement.textContent = data.count;
    }
    

    clickerButton.addEventListener('click', incrementCoinCount);

    getCoinCount();
});

window.addEventListener('scroll', function() {
    // Высота прокрутки
    var scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
    // Высота видимой области
    var clientHeight = document.documentElement.clientHeight || document.body.clientHeight;
    // Текущая позиция прокрутки
    var scrollPosition = window.scrollY || window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;

    // Если страница прокручена до конца
    if (scrollHeight - scrollPosition === clientHeight) {
        // Делаем футер чуть выше
        document.querySelector('.footer').style.bottom = '30px';
    } else {
        // Возвращаем футер в обычное положение
        document.querySelector('.footer').style.bottom = '-10px';
    }
});
