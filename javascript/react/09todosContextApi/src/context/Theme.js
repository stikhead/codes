import React, {useContext} from "react";

const ThemeContext = React.createContext({
    themeMode: 'light',
    onDarkMode: ()=>{},
    onLightMode: ()=>{}
})

export const ThemeProvider = ThemeContext.Provider;

export default function useTheme(){
   return useContext(ThemeContext)
}


