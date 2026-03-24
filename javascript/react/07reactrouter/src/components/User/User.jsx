import { useParams } from "react-router-dom"

export function User(){
    const {userid} = useParams()
    
    return(
        <>
        <h1>parameters: {userid}</h1>
        </>
    )
}