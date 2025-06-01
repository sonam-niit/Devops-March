// Test-suite
describe('My First Test', () => {
    //Test-Case
  it('clicks the link "type"', () => {
    cy.visit('https://example.cypress.io')

    cy.contains('type').click()

    // Should be on a new URL which
    // includes '/commands/actions'
    cy.url().should('include', '/commands/actions')

     // Get an input, type into it
    cy.get('.action-email').type('sonam@email.com')

    //  Verify that the value has been updated
    cy.get('.action-email').should('have.value', 'sonam@email.com')
  })
})