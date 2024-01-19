/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        const word = "Hello World";
        return word;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */