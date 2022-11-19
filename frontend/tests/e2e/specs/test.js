// https://docs.cypress.io/api/table-of-contents

describe('HomeView', () => {
  it('Visits the app root url', () => {
    cy.visit('/')
    cy.contains('h1', 'Welcome to DSA Web Application')
  })
})
