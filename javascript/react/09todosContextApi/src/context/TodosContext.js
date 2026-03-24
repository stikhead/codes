import React, {useContext} from "react"
export const TodosContext = React.createContext({
    todos: [{
        id: Date.now(),
        todoMsg: '',
        completedStatus: false
    }],

    toggleCompleted: ()=>{},
    deleteTodo: ()=>{},
    addTodo: ()=> {},
    updateTodo: ()=>{}
})

export const TodosProvider = TodosContext.Provider;

export default function useTodo(){
    return useContext(TodosContext)
}