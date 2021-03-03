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

export const loadItems = (collection) => {
  let result = []
  if (localStorage.getItem(collection)) {
    try {
      result = JSON.parse(localStorage.getItem(collection));
    } catch(e) {
      localStorage.removeItem(collection);
    }
  }
  return result;
};

export const saveItems = (collection, data) => {
  let parsed = JSON.stringify(data);
  localStorage.setItem(collection, parsed);
};