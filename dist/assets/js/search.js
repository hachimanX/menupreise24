// MenüPreise24.de - Interactive Live Search, Table Filter & Cookie Consent Engine
document.addEventListener('DOMContentLoaded', function () {
  // 1. Cookie Consent Banner (DSGVO / GDPR)
  const cookieBanner = document.getElementById('cookieBanner');
  const cookieAccept = document.getElementById('cookieAcceptBtn');
  const cookieDecline = document.getElementById('cookieDeclineBtn');

  if (cookieBanner) {
    const hasConsent = localStorage.getItem('menupreise24_cookie_consent');
    if (!hasConsent) {
      cookieBanner.style.display = 'block';
    }

    if (cookieAccept) {
      cookieAccept.addEventListener('click', function () {
        localStorage.setItem('menupreise24_cookie_consent', 'accepted');
        cookieBanner.style.display = 'none';
      });
    }

    if (cookieDecline) {
      cookieDecline.addEventListener('click', function () {
        localStorage.setItem('menupreise24_cookie_consent', 'declined');
        cookieBanner.style.display = 'none';
      });
    }
  }

  // 2. Table Item Search & Filter
  const searchInput = document.getElementById('menuSearchInput');
  const filterPills = document.querySelectorAll('.pill-btn');
  const printBtn = document.getElementById('printPdfBtn');
  const tableRows = document.querySelectorAll('.menu-table tbody tr');
  const menuSections = document.querySelectorAll('.menu-section');

  let activeFilter = 'all';
  let searchTerm = '';

  function applyFilters() {
    let visibleCount = 0;

    tableRows.forEach(row => {
      const nameCol = row.querySelector('.item-name')?.textContent.toLowerCase() || '';
      const priceText = row.querySelector('.item-price')?.textContent || '';
      const dietBadge = row.querySelector('.diet-badge')?.textContent.toLowerCase() || '';
      
      const priceMatch = priceText.match(/(\d+[,.]\d+)/);
      const priceNum = priceMatch ? parseFloat(priceMatch[1].replace(',', '.')) : 999;

      const matchesSearch = !searchTerm || nameCol.includes(searchTerm) || dietBadge.includes(searchTerm);

      let matchesPill = true;
      if (activeFilter === 'vegan') {
        matchesPill = dietBadge.includes('vegan');
      } else if (activeFilter === 'veggie') {
        matchesPill = dietBadge.includes('veggie') || dietBadge.includes('vegetarisch') || dietBadge.includes('vegan');
      } else if (activeFilter === 'under5') {
        matchesPill = priceNum > 0 && priceNum <= 5.0;
      } else if (activeFilter === 'under10') {
        matchesPill = priceNum > 0 && priceNum <= 10.0;
      }

      if (matchesSearch && matchesPill) {
        row.style.display = '';
        visibleCount++;
      } else {
        row.style.display = 'none';
      }
    });

    menuSections.forEach(section => {
      const rowsInSection = section.querySelectorAll('tbody tr');
      let sectionHasVisibleRows = false;
      rowsInSection.forEach(r => {
        if (r.style.display !== 'none') sectionHasVisibleRows = true;
      });
      section.style.display = sectionHasVisibleRows ? '' : 'none';
    });

    const countEl = document.getElementById('searchCountBadge');
    if (countEl) {
      if (searchTerm || activeFilter !== 'all') {
        countEl.textContent = `${visibleCount} Treffer`;
        countEl.style.display = 'inline-block';
      } else {
        countEl.style.display = 'none';
      }
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', function (e) {
      searchTerm = e.target.value.toLowerCase().trim();
      applyFilters();
    });
  }

  filterPills.forEach(pill => {
    pill.addEventListener('click', function () {
      filterPills.forEach(p => p.classList.remove('active'));
      this.classList.add('active');
      activeFilter = this.dataset.filter || 'all';
      applyFilters();
    });
  });

  if (printBtn) {
    printBtn.addEventListener('click', function () {
      window.print();
    });
  }

  // 3. FAQ Accordion Toggle
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(q => {
    q.addEventListener('click', function () {
      const answer = this.nextElementSibling;
      const isOpen = answer.style.display !== 'none';
      answer.style.display = isOpen ? 'none' : 'block';
      const icon = this.querySelector('.faq-toggle-icon');
      if (icon) icon.textContent = isOpen ? '+' : '−';
    });
  });

  // 4. Global Home Search Bar
  const globalSearchInput = document.getElementById('globalSearchInput');
  const globalCards = document.querySelectorAll('.brand-search-card');
  if (globalSearchInput && globalCards.length > 0) {
    globalSearchInput.addEventListener('input', function (e) {
      const term = e.target.value.toLowerCase().trim();
      globalCards.forEach(card => {
        const title = card.getAttribute('data-title')?.toLowerCase() || card.textContent.toLowerCase();
        if (!term || title.includes(term)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  }
});
