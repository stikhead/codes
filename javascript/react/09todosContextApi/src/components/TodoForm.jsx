import useTodo from "../context/TodosContext";
import {useState} from 'react'
function TodoForm() {
    const {addTodo} = useTodo();
    const [todo, setTodo] = useState("");
    const [isEmpty, setIsEmpty] = useState(true)
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(todo)
        addTodo(todo)
        setTodo('')
        setIsEmpty(true)
    }
    return (
        <form onSubmit={handleSubmit} 
    className="flex">
            <input
                type="text"
                placeholder="Write Todo..."
                className="w-full border border-black/10 rounded-l-lg px-3 outline-none duration-150 bg-white/20 py-1.5 placeholder-gray-500 dark:placeholder-gray-300"
                value={todo}
                onChange={(e) => (
                    setIsEmpty(false),
                    setTodo(e.currentTarget.value)
                )}
                
            />
            <button
            type="submit" 
            className="rounded-r-lg px-3 py-1 bg-green-600 text-white shrink-0 "
            disabled={isEmpty}
              >
                Add
            </button>
        </form>
    );
}

export default TodoForm;

