from flask import Flask, render_template, request, jsonify
import time
import sys

# Konfigurasi aplikasi Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tubesakaanalisisalgoritma2025'

# Menambah batas rekursi untuk berjaga-jaga input besar
sys.setrecursionlimit(20000)

# ============================================================================
# CORE ALGORITHMS - Dipertahankan dari Streamlit
# ============================================================================

def pangkatRekursif(basis, pangkat):
    """Algoritma pangkat menggunakan pendekatan rekursif"""
    if pangkat == 0:
        return 1    
    return basis * pangkatRekursif(basis, pangkat - 1) 

def pangkatIteratif(basis, pangkat):
    """Algoritma pangkat menggunakan pendekatan iteratif"""
    result = 1
    for i in range(pangkat):
        result *= basis
    return result

def measure_time(func, *args):
    """Mengukur waktu eksekusi fungsi dalam milidetik."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return result, execution_time_ms

# ============================================================================
# ROUTES - Flask Routing
# ============================================================================

@app.route('/')
def index():
    """Redirect ke halaman theory sebagai landing page"""
    return render_template('theory.html')

@app.route('/theory')
def theory():
    """Halaman Teori & Pengantar"""
    return render_template('theory.html')

@app.route('/single-test', methods=['GET', 'POST'])
def single_test():
    """Halaman Single Input Analysis"""
    if request.method == 'POST':
        try:
            # Ambil input dari form
            basis = int(request.form.get('basis', 2))
            pangkat = int(request.form.get('pangkat', 900))
            
            # Validasi input
            if pangkat < 0:
                return jsonify({
                    'success': False,
                    'error': 'Pangkat harus bilangan bulat >= 0'
                })
            
            # Warning untuk rekursi dalam
            warning = None
            if pangkat > 3000:
                warning = 'Pangkat > 3000 dapat menyebabkan RecursionError pada Python standar.'
            
            # Hitung Iteratif
            res_iter, time_iter = measure_time(pangkatIteratif, basis, pangkat)
            
            # Hitung Rekursif
            try:
                res_rec, time_rec = measure_time(pangkatRekursif, basis, pangkat)
                recursion_error = False
            except RecursionError:
                res_rec = None
                time_rec = None
                recursion_error = True
            
            # Validasi hasil
            valid = res_iter == res_rec if not recursion_error else None
            
            # Kesimpulan
            if not recursion_error:
                faster = 'iteratif' if time_iter < time_rec else 'rekursif'
                time_diff = abs(time_iter - time_rec)
                conclusion = f"Algoritma {faster.capitalize()} lebih cepat {time_diff:.6f} ms"
            else:
                conclusion = "Rekursif mengalami RecursionError. Gunakan Iteratif untuk input besar."
            
            return jsonify({
                'success': True,
                'valid': valid,
                'time_iter': time_iter,
                'time_rec': time_rec,
                'recursion_error': recursion_error,
                'conclusion': conclusion,
                'warning': warning,
                'result_iter': str(res_iter) if len(str(res_iter)) < 100 else f"{str(res_iter)[:100]}...",
                'result_rec': str(res_rec) if res_rec and len(str(res_rec)) < 100 else f"{str(res_rec)[:100]}..." if res_rec else None
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })
    
    return render_template('single_test.html')

@app.route('/range-test', methods=['GET', 'POST'])
def range_test():
    """Halaman Range & Graph Analysis"""
    if request.method == 'POST':
        try:
            # Ambil input dari form
            basis = int(request.form.get('basis', 2))
            start_exp = int(request.form.get('start_exp', 10))
            end_exp = int(request.form.get('end_exp', 2000))
            step_exp = int(request.form.get('step_exp', 50))
            
            # Validasi input
            if start_exp >= end_exp:
                return jsonify({
                    'success': False,
                    'error': 'End Pangkat harus lebih besar dari Start Pangkat'
                })
            
            if step_exp <= 0:
                return jsonify({
                    'success': False,
                    'error': 'Interval harus lebih besar dari 0'
                })
            
            # Data collection
            data_points = []
            input_sizes = list(range(start_exp, end_exp + 1, step_exp))
            
            for exp in input_sizes:
                # Ukur Iteratif
                _, t_iter = measure_time(pangkatIteratif, basis, exp)
                
                # Ukur Rekursif (Skip jika terlalu besar untuk mencegah crash)
                if exp > 5000:
                    t_rec = None 
                else:
                    try:
                        _, t_rec = measure_time(pangkatRekursif, basis, exp)
                    except RecursionError:
                        t_rec = None
                
                data_points.append({
                    'input_size': exp,
                    'time_iter': round(t_iter, 6),
                    'time_rec': round(t_rec, 6) if t_rec is not None else None
                })
            
            # Hitung rata-rata
            avg_iter = sum(d['time_iter'] for d in data_points) / len(data_points)
            rec_times = [d['time_rec'] for d in data_points if d['time_rec'] is not None]
            avg_rec = sum(rec_times) / len(rec_times) if rec_times else None
            
            # Kesimpulan
            if avg_rec:
                ratio = avg_rec / avg_iter if avg_iter > 0 else 0
                conclusion = f"Secara rata-rata, Iteratif {ratio:.2f}x lebih cepat daripada Rekursif pada range ini."
            else:
                conclusion = "Data rekursif tidak lengkap (mungkin karena limit rekursi)."
            
            return jsonify({
                'success': True,
                'data_points': data_points,
                'avg_iter': round(avg_iter, 6),
                'avg_rec': round(avg_rec, 6) if avg_rec else None,
                'conclusion': conclusion
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })
    
    return render_template('range_test.html')

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return render_template('theory.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return "Internal Server Error", 500

# ============================================================================
# MAIN
# ============================================================================

# For Vercel serverless
# Export app untuk Vercel
# Jika running locally, jalankan dengan flask run atau python app.py
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
