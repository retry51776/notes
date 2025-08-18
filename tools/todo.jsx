import React, { useState } from "react";

/**
 * Simple Todo list component using React and Bootstrap.
 *
 * Features:
 * - Add new todo items
 * - Mark items as completed / toggle
 * - Remove items
 *
 * The component is self‑contained and can be imported anywhere in the app:
 *   import Todo from "./tools/todo.jsx";
 *
 * Ensure that Bootstrap CSS is loaded in your project (e.g. via CDN or npm package).
 */
const Todo = () => {
  // State for the list of todo items
  const [todos, setTodos] = useState([]);
  // State for the current input value
  const [input, setInput] = useState("");

  // Handler to add a new todo
  const handleAdd = (e) => {
    e.preventDefault();
    const trimmed = input.trim();
    if (!trimmed) return;
    setTodos([
      ...todos,
      { id: Date.now(), text: trimmed, completed: false },
    ]);
    setInput("");
  };

  // Toggle completion status
  const toggleTodo = (id) => {
    setTodos(
      todos.map((t) =>
        t.id === id ? { ...t, completed: !t.completed } : t
      )
    );
  };

  // Remove a todo item
  const removeTodo = (id) => {
    setTodos(todos.filter((t) => t.id !== id));
  };

  return (
    <div className="container my-4">
      <h2 className="mb-3">Todo List</h2>

      {/* Input form */}
      <form onSubmit={handleAdd} className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Enter a new task..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button className="btn btn-primary" type="submit">
          Add
        </button>
      </form>

      {/* Todo items */}
      {todos.length === 0 ? (
        <p className="text-muted">No tasks yet. Add one above!</p>
      ) : (
        <ul className="list-group">
          {todos.map((todo) => (
            <li
              key={todo.id}
              className={`list-group-item d-flex justify-content-between align-items-center ${
                todo.completed ? "list-group-item-success" : ""
              }`}
            >
              <div
                style={{ cursor: "pointer", textDecoration: todo.completed ? "line-through" : "none" }}
                onClick={() => toggleTodo(todo.id)}
              >
                {todo.text}
              </div>
              <button
                className="btn btn-sm btn-outline-danger"
                onClick={() => removeTodo(todo.id)}
              >
                &times;
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Todo;
