from flask import Flask, render_template, request, jsonify, send_file
import time
import sys
import csv
import os
from io import StringIO, BytesIO

# Konfigurasi aplikasi Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-tubesakaanalisisalgoritma2025')

# Menambah batas rekursi (cukup untuk cover batas 5000 di logic)
sys.setrecursionlimit(6000)

# ============================================================================
# CORE ALGORITHMS - Pertumbuhan Bakteri Vibrio natriegens
# ============================================================================

def bakteri_iteratif(n0, x):
    """Algoritma iteratif untuk menghitung pertumbuhan bakteri"""
    hasil = n0
    for i in range(x):
        hasil *= 2
    return hasil

def bakteri_rekursif(n0, x):
    """Algoritma rekursif untuk menghitung pertumbuhan bakteri"""
    if x <= 0:
        return n0
    else:
        return 2 * bakteri_rekursif(n0, x - 1)

def peubah_waktu(satuan_waktu, durasi, laju_pertumbuhan):
    """Mengkonversi waktu menjadi jumlah kejadian pertumbuhan"""
    total_detik = 0
    if satuan_waktu == "1":    # Detik
        total_detik = durasi
    elif satuan_waktu == "2":  # Menit
        total_detik = durasi * 60
    elif satuan_waktu == "3":  # Jam
        total_detik = durasi * 3600 
    elif satuan_waktu == "4":  # Kali (Langsung jumlah kejadian)
        return int(durasi)
    
    # x = Total durasi / Jeda waktu per pertumbuhan
    x = total_detik // laju_pertumbuhan
    return int(x)

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
    """Halaman Single Input Analysis - Pertumbuhan Bakteri"""
    if request.method == 'POST':
        try:
            # Ambil input dari form
            n0 = int(request.form.get('n0', 100))
            tipe_pertumbuhan = request.form.get('tipe_pertumbuhan', '2')
            durasi = float(request.form.get('durasi', 60))
            laju_pertumbuhan = float(request.form.get('laju_pertumbuhan', 10))
            
            # Validasi input
            if n0 <= 0:
                return jsonify({
                    'success': False,
                    'error': 'Jumlah awal bakteri harus > 0'
                })
            
            if laju_pertumbuhan <= 0:
                return jsonify({
                    'success': False,
                    'error': 'Laju pertumbuhan harus > 0'
                })
            
            # Konversi waktu menjadi jumlah kejadian pertumbuhan (x)
            # Laju pertumbuhan dalam menit, konversi ke detik
            laju_detik = laju_pertumbuhan * 60 if laju_pertumbuhan else 0
            x = peubah_waktu(tipe_pertumbuhan, durasi, laju_detik)
            
            # Warning untuk rekursi dalam
            warning = None
            if x > 3000:
                warning = f'Jumlah kejadian ({x}) > 3000 dapat menyebabkan RecursionError pada Python standar.'
            
            # Hitung Iteratif
            res_iter, time_iter = measure_time(bakteri_iteratif, n0, x)
            
            # Hitung Rekursif
            try:
                res_rec, time_rec = measure_time(bakteri_rekursif, n0, x)
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
                conclusion = f"Algoritma {faster.capitalize()} lebih cepat {time_diff:.6f} ms dalam memprediksi populasi bakteri"
            else:
                conclusion = "Rekursif mengalami RecursionError. Gunakan Iteratif untuk input besar."
            
            # Label tipe pertumbuhan
            tipe_label = {
                '1': 'detik',
                '2': 'menit',
                '3': 'jam',
                '4': 'kejadian'
            }
            
            return jsonify({
                'success': True,
                'valid': valid,
                'time_iter': time_iter,
                'time_rec': time_rec,
                'recursion_error': recursion_error,
                'conclusion': conclusion,
                'warning': warning,
                'result_iter': str(res_iter) if len(str(res_iter)) < 100 else f"{str(res_iter)[:100]}...",
                'result_rec': str(res_rec) if res_rec and len(str(res_rec)) < 100 else f"{str(res_rec)[:100]}..." if res_rec else None,
                'input_data': {
                    'n0': n0,
                    'durasi': durasi,
                    'satuan': tipe_label[tipe_pertumbuhan],
                    'laju': laju_pertumbuhan,
                    'kejadian': x
                }
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })
    
    return render_template('single_test.html')

@app.route('/range-test', methods=['GET', 'POST'])
def range_test():
    """Halaman Multiple Test - Pertumbuhan Bakteri"""
    if request.method == 'POST':
        try:
            # Ambil input dari form
            n0 = int(request.form.get('n0', 100))
            tipe_pertumbuhan = request.form.get('tipe_pertumbuhan', '2')
            start_value = float(request.form.get('start_value', 10))
            end_value = float(request.form.get('end_value', 100))
            interval = int(request.form.get('interval', 20))
            laju_pertumbuhan = float(request.form.get('laju_pertumbuhan', 10))
            
            # Validasi input
            if start_value >= end_value:
                return jsonify({
                    'success': False,
                    'error': 'Nilai Akhir harus lebih besar dari Nilai Mulai'
                })
            
            if laju_pertumbuhan <= 0:
                return jsonify({
                    'success': False,
                    'error': 'Laju pertumbuhan harus > 0'
                })
            
            if interval <= 0:
                return jsonify({
                    'success': False,
                    'error': 'Interval harus lebih besar dari 0'
                })
            
            # Laju pertumbuhan dalam menit, konversi ke detik
            laju_detik = laju_pertumbuhan * 60 if laju_pertumbuhan else 0
            
            # Konversi nilai mulai dan akhir ke kejadian
            kejadian_mulai = peubah_waktu(tipe_pertumbuhan, start_value, laju_detik)
            kejadian_akhir = peubah_waktu(tipe_pertumbuhan, end_value, laju_detik)
            
            # Data collection - Generate data points using interval as step on kejadian
            data_points = []
            x = kejadian_mulai
            
            while x <= kejadian_akhir:
                # Ukur Iteratif
                res_iter, t_iter = measure_time(bakteri_iteratif, n0, x)
                
                # Ukur Rekursif (Skip jika terlalu besar untuk mencegah crash)
                if x > 5000:
                    res_rec = None
                    t_rec = None 
                else:
                    try:
                        res_rec, t_rec = measure_time(bakteri_rekursif, n0, x)
                    except RecursionError:
                        res_rec = None
                        t_rec = None
                
                # Format hasil untuk tampilan (ringkas jika terlalu besar)
                result_display = str(res_iter)
                if len(str(res_iter)) > 50:
                    result_display = f"{str(res_iter)[:47]}..."
                
                # Hitung durasi dari kejadian (reverse calculation)
                if tipe_pertumbuhan == '4':  # Kejadian langsung
                    durasi_display = x
                elif tipe_pertumbuhan == '1':  # Detik
                    durasi_display = (x * laju_detik)
                elif tipe_pertumbuhan == '2':  # Menit
                    durasi_display = (x * laju_detik) / 60
                elif tipe_pertumbuhan == '3':  # Jam
                    durasi_display = (x * laju_detik) / 3600
                
                data_points.append({
                    'durasi': round(durasi_display, 2),
                    'kejadian': x,
                    'time_iter': round(t_iter, 6),
                    'time_rec': round(t_rec, 6) if t_rec is not None else None,
                    'result': result_display
                })
                
                # Increment by interval (on kejadian)
                x += interval
            
            # Hitung rata-rata
            avg_iter = sum(d['time_iter'] for d in data_points) / len(data_points)
            rec_times = [d['time_rec'] for d in data_points if d['time_rec'] is not None]
            avg_rec = sum(rec_times) / len(rec_times) if rec_times else None
            
            # Kesimpulan
            if avg_rec:
                ratio = avg_rec / avg_iter if avg_iter > 0 else 0
                conclusion = f"Secara rata-rata, Iteratif {ratio:.2f}x lebih cepat daripada Rekursif dalam memprediksi pertumbuhan bakteri pada range ini."
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

@app.route('/export-range-csv', methods=['POST'])
def export_range_csv():
    """Export multiple test data sebagai CSV - Pertumbuhan Bakteri"""
    try:
        # Ambil input dari form (sama seperti range_test)
        n0 = int(request.form.get('n0', 100))
        tipe_pertumbuhan = request.form.get('tipe_pertumbuhan', '2')
        start_value = float(request.form.get('start_value', 10))
        end_value = float(request.form.get('end_value', 100))
        interval = int(request.form.get('interval', 20))
        laju_pertumbuhan = float(request.form.get('laju_pertumbuhan', 10))
        
        # Validasi input
        if start_value >= end_value or laju_pertumbuhan <= 0 or interval <= 0:
            return jsonify({'success': False, 'error': 'Input tidak valid'}), 400
        
        # Laju pertumbuhan dalam menit, konversi ke detik
        laju_detik = laju_pertumbuhan * 60 if laju_pertumbuhan else 0
        
        # Konversi nilai mulai dan akhir ke kejadian
        kejadian_mulai = peubah_waktu(tipe_pertumbuhan, start_value, laju_detik)
        kejadian_akhir = peubah_waktu(tipe_pertumbuhan, end_value, laju_detik)
        
        # Data collection - Generate data points using interval as step on kejadian
        data_points = []
        x = kejadian_mulai
        
        while x <= kejadian_akhir:
            # Ukur Iteratif
            res_iter, t_iter = measure_time(bakteri_iteratif, n0, x)
            
            # Ukur Rekursif
            if x > 5000:
                res_rec = None
                t_rec = None
            else:
                try:
                    res_rec, t_rec = measure_time(bakteri_rekursif, n0, x)
                except RecursionError:
                    res_rec = None
                    t_rec = None
            
            # Hitung durasi dari kejadian (reverse calculation)
            if tipe_pertumbuhan == '4':  # Kejadian langsung
                durasi_display = x
            elif tipe_pertumbuhan == '1':  # Detik
                durasi_display = (x * laju_detik)
            elif tipe_pertumbuhan == '2':  # Menit
                durasi_display = (x * laju_detik) / 60
            elif tipe_pertumbuhan == '3':  # Jam
                durasi_display = (x * laju_detik) / 3600
            
            data_points.append({
                'durasi': round(durasi_display, 2),
                'kejadian': x,
                'time_iter': round(t_iter, 6),
                'time_rec': round(t_rec, 6) if t_rec is not None else None,
                'result': str(res_iter)
            })
            
            # Increment by interval (on kejadian)
            x += interval
        
        # Buat CSV content sebagai string
        csv_string = StringIO()
        writer = csv.writer(csv_string)
        
        # Header
        writer.writerow(['Durasi', 'Jumlah Kejadian', 'Iteratif (ms)', 'Rekursif (ms)', 'Populasi Bakteri'])
        
        # Data rows
        for point in data_points:
            writer.writerow([
                point['durasi'],
                point['kejadian'],
                point['time_iter'],
                point['time_rec'] if point['time_rec'] is not None else 'N/A',
                point['result']
            ])
        
        # Convert string to bytes
        csv_bytes = BytesIO(csv_string.getvalue().encode('utf-8-sig'))
        
        # Generate filename dengan timestamp
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'bacteria_growth_analysis_{timestamp}.csv'
        
        # Return file
        return send_file(
            csv_bytes,
            mimetype='text/csv',
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        import traceback
        print("Error in export_range_csv:")
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500

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
