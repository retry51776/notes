# js checklist

## General

- Http send variable ALWAYS snake case. Ex: `variable_name_1`

## React

- Split data fetching & ui render into different components.
- Keep a component under 500 lines

## React Component Order

**1. External Info Processing**

Before defining state, process all incoming data.

Destructuring: Always destructure props at the top. `Const { x, y, ...otherProps } = props;`

Hooks: Initialize external hooks like useContext(), useSelector() (Redux), or useLocation() (URL/History).

**2. Internal States**

Define the local data the component needs to manage.

Initialization: Set useState values using the processed external info from Step 1.

Ref Management: Define useRef for DOM references or mutable values that don't trigger re-renders.

**3. Lifecycle & Hooks**

Define `useEffect` for component lifecycle, Dependency Tracking,

**4. Early Exit**
Protect the component from rendering invalid or "not-ready" states.

**5. Event Handlers**
Define the interactivity logic.

Naming Convention: Use the `onXXX` prefix (e.g., onHandleSubmit).

State Updates: This is where the primary business logic for user interaction lives.

**6. UI Components & Rendering**
Keep the return statement clean and focused on structure.

Sub-components: For complex sections, create buildXXX functions or separate JSX elements.

Optimization: Wrap expensive UI calculations in useMemo and functions passed to children in useCallback.

Logic-Free JSX: Avoid complex ternary operators or mapping logic directly inside the main return.
