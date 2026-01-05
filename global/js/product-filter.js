document.addEventListener('DOMContentLoaded', () => {
  const searchProducts = document.querySelector('input[name="products"]')
  const searchDesks = document.querySelector('input[name="desks"]')
  const categoryButtons = document.querySelectorAll('.categories button')
  const products = document.querySelectorAll('.products-container .product')
  const desks = document.querySelectorAll('.desks-container .desk')

  let activeCategory = null

  function normalize(text) {
    return text
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .toLowerCase()
  }

 function filterProducts() {
  const searchText = normalize(searchProducts.value)

  products.forEach(product => {
    const name = normalize(product.querySelector('p').innerText)

    const matchesName = name.includes(searchText)
    const matchesCategory =
      !activeCategory || itemHasClass(product, activeCategory)

    product.style.display =
      matchesName && matchesCategory ? 'flex' : 'none'
  })
}

function filterDesks() {
  const searchText = normalize(searchDesks.value)

  desks.forEach(desk => {
    const number = normalize(desk.querySelector('h3').innerText)

    const matchesNumber = number.includes(searchText)
    const matchesClients =
      !activeCategory || itemHasClass(desk, activeCategory)

    desk.style.display =
      matchesNumber && matchesCategory ? 'flex' : 'none'
  })
}

function itemHasClass(product, category) {
  return Array.from(product.classList).some(cls => {
    return normalize(cls) === category
  })
}


  // 🔍 Busca por nome
  searchProducts.addEventListener('input', filterProducts)
  searchDesks.addEventListener('input', filterDesks)

  // 🏷️ Filtro por categoria + estado ativo
  categoryButtons.forEach(button => {
    button.addEventListener('click', () => {
      const category = normalize(button.innerText)

      // 👉 Desativar se clicar na mesma categoria
      if (activeCategory === category) {
        activeCategory = null
        button.classList.remove('active')
      } else {
        activeCategory = category

        categoryButtons.forEach(b => b.classList.remove('active'))
        button.classList.add('active')
      }

      filterProducts()
    })
  })
})
