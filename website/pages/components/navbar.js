import styles from '../../styles/Home.module.scss'
import rc from '../../styles/rowcrop.module.css'
import Link from 'next/link'
import StaticImage from './static_image.js'

export default function NavBar() {
    return (
        <nav className={styles.nav}>
            <div> 
                <Link href="/" passHref>
                    <a id={styles.logo}><StaticImage src="/wordmark.svg" /></a>
                </Link>
            </div>
            <div>
                <Link href="/tutorial"><a>Tutorials</a></Link>
                <Link href="/docs"><a>Docs</a></Link>
            </div>
            <div>
                <Link href="https://github.com/tfukaza/harvest">
                <a className={`${rc.button} ${styles.github}`}>
                GitHub</a>
                </Link>
            </div>
           
        </nav>
    )
}

