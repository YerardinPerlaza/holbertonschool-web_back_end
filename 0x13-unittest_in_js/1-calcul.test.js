const assert = require('assert').strict;
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  describe('sUM no Round', () => {
    it('should return 5', () => {
	    assert.equal(calculateNumber('SUM', 1, 4), 5);
    });
  });

  describe('sUM first round', () => {
    it('should return 6', () => {
	    assert.equal(calculateNumber('SUM', 2.4, 4), 6);
    });
  });

  describe('sUM second round', () => {
    it('should return 6', () => {
	    assert.equal(calculateNumber('SUM', 4, 2.4), 6);
    });
  });

  describe('sUM both round', () => {
    it('should return 6', () => {
	    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('sUBTRACT no round', () => {
    it('should return 2', () => {
	    assert.equal(calculateNumber('SUBTRACT', 5, 3), 2);
    });
  });

  describe('sUBTRACT first round', () => {
    it('should return -3', () => {
	    assert.equal(calculateNumber('SUBTRACT', 2, 4.5), -3);
    });
  });

  describe('sUBTRACT second round', () => {
    it('should return 3', () => {
	    assert.equal(calculateNumber('SUBTRACT', 4.5, 2), 3);
    });
  });

  describe('sUBTRACT both round', () => {
    it('should return -4', () => {
	    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
  });

  describe('dIVIDE no round', () => {
    it('should return 2', () => {
	    assert.equal(calculateNumber('DIVIDE', 8, 4), 2);
    });
  });

  describe('dIVIDE first round', () => {
    it('should return 5', () => {
	    assert.equal(calculateNumber('DIVIDE', 9.5, 2), 5);
    });
  });

  describe('dIVIDE second round', () => {
    it('should return 0.2', () => {
	    assert.equal(calculateNumber('DIVIDE', 2, 9.5), 0.2);
    });
  });

  describe('dIVIDE both round', () => {
    it('should return 0.2', () => {
	    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
  });

  describe('dIVIDE Error', () => {
    it('should return Error', () => {
	    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
});
