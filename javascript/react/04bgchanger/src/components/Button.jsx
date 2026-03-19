export function Button({color, c}){

    

    return (
        <button 
            onClick={()=> c(color)}
            className="px-4 py-2 text-white rounded"
            style={{ backgroundColor: color }}
            >
                {color}
            </button>
    )
}