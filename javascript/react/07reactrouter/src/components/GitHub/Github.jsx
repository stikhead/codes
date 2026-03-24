// import {useEffect, useState} from 'react'
import { useLoaderData } from 'react-router-dom';

export function Gihtub(){
    const data = useLoaderData();
    // const [data, setData] = useState({});
    // useEffect(()=>{
    //     let url = 'https://api.github.com/users/stikhead'
    //     fetch(url)
    //     .then((res) => res.json())
    //     .then((res) => setData(res));
    // }, [])
    
    return(
        <>
        <h1>Github Followers: {data.followers}</h1>
        <img src={data.avatar_url} alt="git picture" width='300'/>
        </>
    )
}
let cache = {
    data: null,
    timestamp: 0
};

const CACHE_TIME = 1000 * 60;

export const githubInfoLoader = async ()=>{
    const now = Date.now();

    if (cache.data && (now - cache.timestamp < CACHE_TIME)) {
        return cache.data;
    }

    const response = await fetch('https://api.github.com/users/stikhead', { cache: "force-cache" });
    const data = await response.json();

    cache = {
        data,
        timestamp: now
    };

    return data;
}