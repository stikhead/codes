import TodoForm from "./components/TodoForm"
import TodoItem from "./components/TodoItem"
import Button from "./components/Button"
import { ThemeProvider } from "./context/Theme"
import { TodosProvider } from "./context/TodosContext"
import { useState, useEffect } from 'react'

function App() {
  const [todos, setTodos] = useState(() => {
      const savedTodos = localStorage.getItem('todoslist');
      return savedTodos ? JSON.parse(savedTodos) : [];
    });
const [themeMode, setThemeMode] = useState(() => {
    const savedTheme = localStorage.getItem('theme');
    return savedTheme ? JSON.parse(savedTheme) : 'light';
  });

  const addTodo = (todo) => {

    setTodos( (prevTodos)=> [ 
      { 
        ...todo,
        id: Date.now(),
        todoMsg: todo
        
      }, ...prevTodos])
      console.log(todos)
  }

  const deleteTodo = (id) => {
    setTodos( (prevTodos) => 
        prevTodos.filter( (todos) => 
          todos.id!==id         
      )
    )
  }

  const toggleCompleted = (id) => {
    setTodos( (prevTodos) => 
      prevTodos.map( (todos) => (
        todos.id!==id ? todos : {...todos, completedStatus: !todos.completedStatus}
      ))
    )
  }

  const updateTodo = (id, todo)=>{
    setTodos((prevTodos)=>prevTodos.map((todos)=>todos.id===id ? {...todos, todoMsg: todo} : todos))
  }

  const onDarkMode = ()=> {
    setThemeMode('dark')
  }

  
  const onLightMode = ()=> {
    setThemeMode('light')
  }

  useEffect(()=>{
         document.querySelector('html').classList.remove('light', 'dark')
      document.querySelector('html').classList.add(themeMode)
      localStorage.setItem('theme', JSON.stringify(themeMode))
  }, [themeMode])

  useEffect(()=>{

      localStorage.setItem("todoslist", JSON.stringify(todos))
  }, [todos, setTodos])

  return (
    <ThemeProvider value={{ onLightMode, onDarkMode, themeMode }}>
      <TodosProvider value={{ todos, toggleCompleted, addTodo, deleteTodo, updateTodo }}>
        <div className="min-h-screen py-8">
          <div className="w-full max-w-2xl mx-auto shadow-md rounded-lg px-4 py-3 text-gray-900 bg-gray-100 dark:bg-gray-800 dark:text-white border dark:border-gray-700">
            <h1 className="text-2xl font-bold dark:text-white text-blue-600 text-center mb-8 mt-2">
              Manage Your Todos
            </h1>
            <div>
              <Button />
            </div>
            <div className="mb-4">
              <TodoForm />
            </div>
            <div className="flex flex-wrap gap-y-3">
              {todos.map((todo) => (
                <div key={todo.id} className="w-full">
                  <TodoItem todo={todo} />
                </div>
              ))}
            </div>
          </div>
        </div>
      </TodosProvider>
    </ThemeProvider>
  );
}

export default App
