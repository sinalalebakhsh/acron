import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

function Login() {
    const { login } = useContext(AuthContext);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        const result = await login(username, password);
        
        setLoading(false);
        if (!result.success) {
            setError(result.error);
        }
    };

    return (
        <div style={styles.container}>
            <div style={styles.card}>
                <h2 style={styles.title}>ورود به سیستم Acron</h2>
                
                {error && <div style={styles.error}>{error}</div>}
                
                <form onSubmit={handleSubmit} style={styles.form}>
                    <div style={styles.inputGroup}>
                        <label style={styles.label}>نام کاربری:</label>
                        <input 
                            type="text" 
                            value={username} 
                            onChange={(e) => setUsername(e.target.value)} 
                            style={styles.input}
                            required 
                        />
                    </div>
                    
                    <div style={styles.inputGroup}>
                        <label style={styles.label}>رمز عبور:</label>
                        <input 
                            type="password" 
                            value={password} 
                            onChange={(e) => setPassword(e.target.value)} 
                            style={styles.input}
                            required 
                        />
                    </div>
                    
                    <button type="submit" style={styles.button} disabled={loading}>
                        {loading ? 'در حال بررسی...' : 'ورود'}
                    </button>
                </form>
            </div>
        </div>
    );
}

// استایل‌های درون‌برنامه‌ای ساده برای ظاهر فرم
const styles = {
    container: { display: 'flex', justifyContent: 'center', alignItems: 'center', height: '80vh', fontFamily: 'sans-serif' },
    card: { padding: '30px', borderRadius: '8px', boxShadow: '0 4px 15px rgba(0,0,0,0.1)', width: '350px', backgroundColor: '#fff', direction: 'rtl' },
    title: { textAlign: 'center', marginBottom: '20px', color: '#333' },
    form: { display: 'flex', flexDirection: 'column' },
    inputGroup: { marginBottom: '15px' },
    label: { display: 'block', marginBottom: '5px', fontWeight: 'bold', color: '#555' },
    input: { width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc', boxSizing: 'border-box' },
    button: { padding: '10px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' },
    error: { backgroundColor: '#ffebee', color: '#c62828', padding: '10px', borderRadius: '4px', marginBottom: '15px', textAlign: 'center', fontSize: '14px' }
};

export default Login;

