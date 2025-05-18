const assert = require('assert')
const { add } = require('../src')
describe('Addition Function',()=>{
    it('should return 5 for add(2,3)',()=>{
        assert.strictEqual(add(2,3),5)
    })

    it('should return -1 for add(-2,1)',()=>{
        assert.strictEqual(add(-2,1),-1)
    })

    it('should return 0 for add(-2,2)',()=>{
        assert.strictEqual(add(-2,2),0)
    })
})