# NextJs
> allow bot scan, faster load time, able CDN

## Structure
- /pages `file name routing`
    - /api `similar express default (req, res) => {}`
    - /sales
        - index.js
        - /[id].js `/sales/123`

```
import { useRouter } from 'next/router';
import styles from '/styles/Home.css'

# Runs in Server side
export async function getStaticPaths() {
    return {
        paths: [
            {
                params: {
                    id: 'XXX',
                }
            },
            {
                params: {
                    id: 'YYY',
                }
            }
        ],
        fallback: false,
    };
}

# Runs in client side
export async function getStaticProps() {
    const req = await fetch('/sales');
    const sales = await req.json();
    return {
        props: {
            sales,
        },
        revalidate: 30, # cache 30s
    }
}

export default function Sales({ sales }) {
    const router = useRoute();
    return (
        <h1 className={styles.header}>
            {router.query.id}
        </h1>
    );
}

```