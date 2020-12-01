# What is React?
- Declarative
- Efficient
- Flexible
- JavaScript library
- For building user interfaces
- Compose complex UIs from small and isolated
  pieces of code called "components"

# React.Component
- We use components to tell React what we want to see
  on the screen
- When the data changes, React will efficiently update and re-render our components
- A component takes in parameters, props
- Returns a hierarchy of views to display via the render
  method

# render
- render method returns a description of what you want to see on the screen
- React takes the description and displays the result
- render returns a React Element, lightweight description of what to render
- Use JSX

# parent and children
To collect data from multiple children, or to have two child components communicate with each other, you need to declare the shared state in their parent component instead. The parent component can pass the state back down to the children by using props; this keeps the child components in sync with each other and with the parent component.