// Variables principales
    let money = 0;
    let totalEarned = 0;
    let perClick = 1;
    let perSecond = 0;
    let upgradesBought = 0;

    // Costos de upgrades
    let clickUpgradeCost = 10;
    let idleUpgradeCost = 25;
    let autoUpgradeCost = 200;

    // Multiplicadores
    let clickUpgradeMult = 1;
    let idleUpgradeMult = 1;
    let autoUpgradeMult = 5;

    // Actualiza UI
    function updateUI() {
      document.getElementById('money').textContent = money;
      document.getElementById('perClick').textContent = perClick;
      document.getElementById('perSecond').textContent = perSecond;
      document.getElementById('totalEarned').textContent = totalEarned;
      document.getElementById('upgradesBought').textContent = upgradesBought;
      document.getElementById('clickUpgradeCost').textContent = clickUpgradeCost;
      document.getElementById('idleUpgradeCost').textContent = idleUpgradeCost;
      document.getElementById('autoUpgradeCost').textContent = autoUpgradeCost;
    }

    // Clicker principal
    document.getElementById('clickerBtn').addEventListener('click', () => {
      money += perClick;
      totalEarned += perClick;
      updateUI();
      // Animación feedback
      const btn = document.getElementById('clickerBtn');
      btn.classList.add('ring-4', 'ring-amber-400');
      setTimeout(() => btn.classList.remove('ring-4', 'ring-amber-400'), 150);
    });

    // Idle loop
    setInterval(() => {
      if (perSecond > 0) {
        money += perSecond;
        totalEarned += perSecond;
        updateUI();
      }
    }, 1000);

    // Comprar upgrades
    function buyUpgrade(type) {
      if (type === 'click' && money >= clickUpgradeCost) {
        money -= clickUpgradeCost;
        perClick += clickUpgradeMult;
        clickUpgradeCost = Math.floor(clickUpgradeCost * 1.5);
        upgradesBought += 1;
      }
      if (type === 'idle' && money >= idleUpgradeCost) {
        money -= idleUpgradeCost;
        perSecond += idleUpgradeMult;
        idleUpgradeCost = Math.floor(idleUpgradeCost * 1.7);
        upgradesBought += 1;
      }
      if (type === 'autoclicker' && money >= autoUpgradeCost) {
        money -= autoUpgradeCost;
        perSecond += autoUpgradeMult;
        autoUpgradeCost = Math.floor(autoUpgradeCost * 2.2);
        upgradesBought += 1;
      }
      updateUI();
    }

    // Tienda desplegable
    const shopPanel = document.getElementById('shopPanel');
    document.getElementById('toggleShop').addEventListener('click', () => {
      shopPanel.classList.toggle('-translate-x-full');
    });
    document.getElementById('closeShop').addEventListener('click', () => {
      shopPanel.classList.add('-translate-x-full');
    });

    // Inicializa UI
    updateUI();