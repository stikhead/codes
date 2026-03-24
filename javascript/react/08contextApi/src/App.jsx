import { useEffect, useState } from "react"
import { ThemeProvider } from "./context/theme"
import Card from "./components/Card";
import Button from "./components/Button"
function App() {
 
  const [themeMode, setThemeMode] = useState('light');
  const onDarkMode = () => {
    setThemeMode('dark')
  }

  const onLightMode = () => {
    setThemeMode('light')
  }

  useEffect(() => {
    document.querySelector('html').classList.remove('light', 'dark');
    document.querySelector('html').classList.add(themeMode)
  }, [themeMode])


  return (
    <ThemeProvider value={{themeMode, onDarkMode, onLightMode}}>
            <div className="flex flex-wrap min-h-screen items-center">
                <div className="w-full">
                    <div className="w-full max-w-sm mx-auto flex justify-end mb-4">
                        <Button/>
                    </div>

                    <div className="w-full max-w-sm mx-auto">
                       <Card/>
                    </div>
                </div>
            </div>

     </ThemeProvider>
  )
}

export default App
