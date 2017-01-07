module.exports = {
  root: true,
  parser: 'babel-eslint',
  parserOptions: {
    sourceType: 'module'
  },
  // https://github.com/feross/standard/blob/master/RULES.md#javascript-standard-style
  extends: 'standard',
  // required to lint *.vue files
  plugins: [
    'html'
  ],
  // add your custom rules here
  'rules': {
    // allow paren-less arrow functions
    'arrow-parens': 0,
    // allow async-await
    'generator-star-spacing': 0,
    // no space between the method name and the parenthesis
    'space-before-function-paren': 0,
    // allow multiple appears at the end of a comma
    'comma-dangle': ["error", "ignore"],
    // allow the head annotation
    'no-trailing-spaces': 0,
    // allow you to define multiple variables
    "one-var": 0,
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0
  }
}
