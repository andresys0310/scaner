$file = "Contenido-Mail.txt"

if (test-path $file)
{

    $from = "guillermo.cepeda@uniminuto.edu"
    $to = "guillermo.cepeda@uniminuto.edu","jorge.sierra@uniminuto.edu"
    #Las direcciones del to deben indicarse con signos de mayor que 
    #y menor que.
    $pc = get-content env:computername
    $subject = "Mesaje de prueba del servidor " + $pc
    $smtpserver = "10.0.30.73"


    #Con Out-String formateamos el texto
    $body = Get-Content $file | Out-String


    foreach ($recipient in $to)
    {
        write-host "Enviando mail a $to"
        Send-MailMessage -smtpServer $smtpserver -from $from -to $recipient -subject $subject  -body $body
    }
}
else
{
write-host "Fichero no encontrado"
}