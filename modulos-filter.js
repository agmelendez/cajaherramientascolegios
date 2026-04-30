document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const filterNivel = document.getElementById('filterNivel');
    const filterProposito = document.getElementById('filterProposito');
    const filterTrimestre = document.getElementById('filterTrimestre');
    const filterTipo = document.getElementById('filterTipo');
    
    const pill15min = document.getElementById('pill15min');
    const pillDua = document.getElementById('pillDua');
    const pillEtica = document.getElementById('pillEtica');
    const btnLimpiar = document.getElementById('btnLimpiar');

    const modulesGrid = document.getElementById('modulesGrid');
    const cards = Array.from(modulesGrid.querySelectorAll('.module-card'));
    const noResults = document.getElementById('noResults');

    let activePills = {
        '15min': false,
        'dua': false,
        'etica': false
    };

    function filterCards() {
        const query = searchInput.value.toLowerCase();
        const nivel = filterNivel.value;
        const proposito = filterProposito.value;
        const trimestre = filterTrimestre.value;
        const tipo = filterTipo.value;

        let visibleCount = 0;

        cards.forEach(card => {
            const cardTitle = card.querySelector('h3').textContent.toLowerCase();
            const cardDesc = card.querySelector('p').textContent.toLowerCase();
            const textMatch = cardTitle.includes(query) || cardDesc.includes(query);

            const nMatch = !nivel || card.dataset.nivel === nivel;
            const pMatch = !proposito || card.dataset.proposito === proposito;
            const tMatch = !trimestre || card.dataset.trimestre === trimestre;
            const tipoMatch = !tipo || card.dataset.tipo === tipo;

            let pillMatch = true;
            if (activePills['15min'] && card.dataset.duracion !== 'corta') pillMatch = false;
            if (activePills['dua'] && !card.dataset.tags?.includes('dua')) pillMatch = false;
            if (activePills['etica'] && !card.dataset.tags?.includes('etico')) pillMatch = false;

            if (textMatch && nMatch && pMatch && tMatch && tipoMatch && pillMatch) {
                card.style.display = 'flex';
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });

        if (visibleCount === 0) {
            noResults.classList.remove('hidden');
        } else {
            noResults.classList.add('hidden');
        }
    }

    [searchInput, filterNivel, filterProposito, filterTrimestre, filterTipo].forEach(el => {
        el.addEventListener('input', filterCards);
    });

    function togglePill(pillBtn, key) {
        activePills[key] = !activePills[key];
        if (activePills[key]) {
            pillBtn.classList.replace('bg-gray-50', 'bg-blue-50');
            pillBtn.classList.replace('text-gray-600', 'text-mep-blue');
            pillBtn.classList.replace('border-gray-200', 'border-blue-100');
        } else {
            pillBtn.classList.replace('bg-blue-50', 'bg-gray-50');
            pillBtn.classList.replace('text-mep-blue', 'text-gray-600');
            pillBtn.classList.replace('border-blue-100', 'border-gray-200');
        }
        filterCards();
    }

    pill15min.addEventListener('click', () => togglePill(pill15min, '15min'));
    pillDua.addEventListener('click', () => togglePill(pillDua, 'dua'));
    pillEtica.addEventListener('click', () => togglePill(pillEtica, 'etica'));

    btnLimpiar.addEventListener('click', () => {
        searchInput.value = '';
        filterNivel.value = '';
        filterProposito.value = '';
        filterTrimestre.value = '';
        filterTipo.value = '';
        if (activePills['15min']) togglePill(pill15min, '15min');
        if (activePills['dua']) togglePill(pillDua, 'dua');
        if (activePills['etica']) togglePill(pillEtica, 'etica');
        filterCards();
    });
});
