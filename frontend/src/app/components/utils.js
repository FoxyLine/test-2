const DOMAIN = "http://localhost:8000/"
const API_ROOT = DOMAIN + "api/"


export const applyDrag = (arr, dragResult) => {
    const { removedIndex, addedIndex, payload } = dragResult;
    if (removedIndex === null && addedIndex === null) return arr;
    const result = [...arr];
    let itemToAdd = payload;
    if (removedIndex !== null) {
        itemToAdd = result.splice(removedIndex, 1)[0];
    }
    if (addedIndex !== null) {
        result.splice(addedIndex, 0, itemToAdd);
    }
    return result;
};

export let createCard = (text, collection) => {
    return fetch(API_ROOT + "cards/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            Authorization: "Token " + localStorage.getItem('token'),
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            text: text,
            type: collection
        })
    }).then(
        response => {
            return response.json()
        }
    )
}

export let moveCard = (card, collection, newIndex) => {
    return fetch(API_ROOT + `cards/${card.id}/change_desk/?type=${collection}&order=${newIndex}`, {
        method: "PUT",
        credentials: "same-origin",
        headers: {
            Authorization: "Token " + localStorage.getItem('token'),
            'Content-Type': 'application/json;charset=utf-8'
        }
    }).then(
        response => {
            return response.json()
        }
    )
}

export let deleteCard = (index) => {
    return fetch(API_ROOT + "cards/" + index, {
        method: "DELETE",
        credentials: "same-origin",
        headers: {
            Authorization: "Token " + localStorage.getItem('token'),
            'Content-Type': 'application/json;charset=utf-8'
        }
    })
}


export const loadCards = () => {
    return fetch(API_ROOT + "cards/", {
        method: "GET",
        credentials: "same-origin",
        headers: {
            Authorization: "Token " + localStorage.getItem('token')
        }
    }).then(response => {
        return response.json()
    })
}

export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export const signin = (body) => {
    let formData = new FormData();

    formData.append('username', body.username)
    formData.append('password', body.password)
    formData.append('csrfmiddlewaretoken', getCookie('csrftoken'))

    return fetch(DOMAIN +"auth-token/", {
            method: "POST",
            credentials: "same-origin",
            body: formData
        })
        .then(response => response.json())

}